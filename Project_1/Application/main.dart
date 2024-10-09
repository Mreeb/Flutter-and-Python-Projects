import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Project 1",
      theme: ThemeData(primaryColor: Colors.black),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final TextEditingController _controller = TextEditingController();
  String _response = '';

  Future<void> sendRequest(String name) async {
    final String apiurl = 'http://192.168.100.128:8000/story';
    // setState(() {
    //   _response = 'Loading...'; // Reset response to indicate loading state
    // });
    try {
      final response = await http.post(Uri.parse(apiurl), headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      }, body: {
        'name': name,
      });

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        setState(() {
          _response = data['story'];
        });
      } else {
        setState(() {
          _response = 'Failed to load story';
        });
      }
    } catch (e) {
      setState(() {
        _response = 'Error: $e';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      appBar: PreferredSize(
        preferredSize: const Size.fromHeight(35),
        child: AppBar(
          title: Padding(
            padding: const EdgeInsets.all(8.0),
            child: Center(
              child: Text(
                "My Story",
                style: TextStyle(fontSize: 30),
              ),
            ),
          ),
          backgroundColor: const Color.fromARGB(255, 80, 44, 14),
        ),
      ),
      body: Container(
        padding: const EdgeInsets.all(20.0),
        child: SingleChildScrollView(
          child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: Column(
              children: [
                TextField(
                    controller: _controller,
                    keyboardType: TextInputType.emailAddress,
                    style: TextStyle(color: Colors.blueGrey),
                    cursorColor: Colors.blueGrey,
                    decoration: InputDecoration(
                        prefixIcon: IconButton(
                            onPressed: () {
                              print("Prefix Icon Pressed");
                            },
                            icon: const Icon(
                              Icons.person,
                              color: Color.fromARGB(255, 80, 44, 14),
                            )),
                        suffixIcon: IconButton(
                            onPressed: () {
                              print("Request Sent");
                              sendRequest(_controller.text);
                            },
                            icon: Icon(
                              Icons.send,
                              color: Color.fromARGB(255, 80, 44, 14),
                            )),
                        labelText: "Enter your Name",
                        labelStyle: const TextStyle(
                            color: Color.fromARGB(255, 80, 44, 14)),
                        errorBorder: const OutlineInputBorder(
                            borderSide:
                                BorderSide(color: Colors.red, width: 2)),
                        enabledBorder: const OutlineInputBorder(
                            borderSide:
                                BorderSide(color: Colors.white, width: 2)),
                        focusedBorder: const OutlineInputBorder(
                            borderSide: BorderSide(color: Colors.blueGrey)))),
                SizedBox(
                  height: 10,
                ),
                Text(
                  "${_response.toString()}",
                  style: TextStyle(
                      color: Color.fromARGB(255, 116, 98, 84), fontSize: 20),
                  textAlign: TextAlign.center,
                )
              ],
            ),
          ),
        ),
      ),
    );
  }
}
