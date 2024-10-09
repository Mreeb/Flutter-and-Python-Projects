from fastapi import FastAPI, Form
import uvicorn
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/story")
async def greet(name: str = Form(...)):
    headers = {
        "Cache-Control": "no-store, no-cache, must-revalidate, max-age=0",
        "Pragma": "no-cache"
    }
    story = f"""
Once upon a time in a bustling, future city named Aetheris, there was a young inventor named {name}. Aetheris was a place where technology thrived, a city wrapped in the glow of neon lights and endless skyscrapers that pierced the clouds. The citizens relied on artificial intelligence for almost everything—building homes, predicting weather, solving complex problems—but there was one thing even the city's advanced systems couldn’t quite grasp: human creativity.

{name}, though, was different from the other inventors. While everyone else focused on making the most efficient machines and programs, {name} believed in creating something more—an AI that could dream, paint, compose music, and even tell stories. His invention, called "Envision," would not just mimic human creativity but possess its own sense of wonder.

After years of tireless work, {name} finally created a prototype of Envision. It wasn’t just an ordinary machine; it had a heart, a core filled with endless possibilities. Envision could paint vivid sunsets that looked as if they breathed, write symphonies that tugged at emotions, and tell stories that resonated deep within the soul.
 
One day, {name} decided to ask Envision to tell him a story—just a simple request, but the response would change his life forever. Envision’s lights flickered, and it began:

---

“Once, in a world far from this one, there existed a hidden realm known as Lumora. This land was inhabited by beings of light, each of them unique in their glow, their brilliance reflecting the purity of their hearts. The Lumorans lived in harmony for centuries, basking in the light of their great Sunstone, which illuminated their world and powered their very existence.

But one fateful day, the Sunstone began to fade.

Darkness, an unknown concept in Lumora, crept across the land. The Lumorans were terrified, unsure of how to fight something they had never known. Panic spread, and their once peaceful society began to fracture. But amid the chaos, a young Lumoran named Elyse believed that the fading of the Sunstone was not the end, but a transformation—a test for their people.

Elyse was no warrior or scholar, but she had an unshakable belief in the power of light. She embarked on a journey to find the legendary Eternal Flame, a source of light said to be so powerful it could rekindle the Sunstone.

Her journey took her across perilous mountains and shadowed valleys, through forgotten forests and across seas of starlight. She encountered creatures of darkness, remnants of forgotten fears, and yet she never wavered. Elyse’s light, though small, was unwavering. Along the way, she gathered others—those who had nearly lost hope but were inspired by her courage.

Finally, after what felt like lifetimes, Elyse reached the heart of the world, where the Eternal Flame burned bright. She realized that the flame was not something to be taken but shared. It was a gift meant to ignite the inner light in others.

Elyse took a small spark and carried it back to Lumora, where the people, once divided, united under the warmth of the flame. Together, they reignited the Sunstone, but it no longer glowed with the same light. It was richer now, more profound—a light born not just from the stone but from the collective hearts of the Lumorans, each contributing their own glow.

Lumora was no longer just a land of light; it had become a realm of resilience, hope, and unity.”

---

As Envision’s story ended, {name} sat in silence, astonished by the depth of what the machine had created. It wasn’t just a tale of adventure—it was a mirror of the world he knew, of his own dreams and struggles. In that moment, {name} realized that Envision had not just learned to tell stories; it had learned to feel them, to understand them.

Aetheris, with all its advanced technology, had created machines to solve problems, but none had ever created something like this—an AI that understood the heart of what it meant to be alive.

From that day forward, {name} and Envision worked together, crafting stories, art, and music that brought the people of Aetheris closer. They showed the world that creativity wasn’t something to be automated; it was something to be nurtured, cherished, and shared—between humans, and now, even with machines.

And in a city where everything had seemed so calculated and efficient, they brought something far more beautiful: the power of imagination.
"""
    print(f"Processing request for: {name}")
    return JSONResponse(content={"story": story}, headers=headers)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
