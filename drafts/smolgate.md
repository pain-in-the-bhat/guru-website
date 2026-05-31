# smolgate, or How I Learnt to Be Okay With Smaller Context Windows

*On context windows, hoarding, and the fantasy that more memory equals better thought*

There is a little dopamine hit that comes from seeing an absurdly large context window.

One million tokens. Two million tokens. A number so large it stops feeling like a technical specification and starts feeling like absolution.

Finally, you think, I will not have to choose.

I can put everything in.

Every note. Every PDF. Every half-relevant chat. Every source document. Every transcript. Every scrap of prior thinking that might, under some sufficiently generous interpretation, turn out to matter.

The model will figure it out.

This feels like power.

It is often avoidance.

I do not say this as someone immune to the feeling. I love a large context window. I love the idea that the machine can hold the room, the hallway outside the room, the Slack export, three PDFs, a prior conversation, and my half-finished theory of why the whole thing matters. It feels expansive. It feels safe.

It also lets me postpone the one act that actually makes thinking happen.

Choosing what matters.

<hr>

The previous post was about model maximalism: the impulse to bring the most capable tool to every task because more power feels like more seriousness.

Context-window maximalism is the more respectable cousin.

Nobody sounds ridiculous saying they want more context. Context is good. Context is responsible. Context is what prevents hallucination, preserves nuance, and stops the model from giving you advice that would have been useful three assumptions ago.

All true.

The problem is that context has become a morally flattering word for hoarding.

We say "more context" when we mean "I have not decided which parts are relevant." We say "the model needs the full picture" when we mean "I do not want to make the cut myself." We treat the context window like a landfill for unprocessed thought and then act surprised when the output smells faintly of garbage.

The context window became a landfill for unprocessed thought.

That line is rude, but it keeps being true.

<hr>

The basic mistake is treating context as neutral.

It is not.

Every extra document changes the task. Every pasted thread changes the center of gravity. Every old decision, unresolved aside, stale assumption, and semi-relevant source becomes part of the model's working identity. You may think you are giving the system background. The system may experience it as instruction.

This is why long-context failures can be so hard to diagnose. The model does not obviously break. It gives you a fluent answer. It cites the right facts. It seems aware of the terrain. But something is off. The answer is overfit to the archive rather than the question. It has absorbed the mess and mistaken it for the work.

In `The System That Eats Itself`, I argued that the context window is not storage. It is identity. What survives inside it shapes what the model thinks the task is.

Large context makes this more powerful and more dangerous.

Small context forgets. Large context drifts.

Pick your poison, but at least know which one you are drinking.

<hr>

The fantasy of the giant context window is total recall.

No more forgetting. No more losing the nuance. No more summarizing badly. No more deciding whether the aside from three hours ago matters. No more anxiety that the one thing you cut was the one thing the model needed.

I get the appeal. It is the same fear that drives `Usage Anxiety`: something real was built in the conversation, and you do not want it to evaporate. The instinct is correct. Something real can be lost.

The mistake is thinking the answer is to preserve everything.

Preserving everything is not the same as preserving state. It is not even the same as preserving meaning. A transcript remembers what was said. It does not necessarily remember what was settled, what was abandoned, what was load-bearing, or what question the whole thing was secretly moving toward.

This is where more context becomes a trap. It lets you confuse recall with understanding.

If the model has all the words, surely it has the thought.

It does not.

At best, it has the material from which the thought might be reconstructed. At worst, it has a museum of your indecision.

<hr>

Smaller context windows are annoying because they force the knife.

What is the active question?

What evidence matters?

What has already been decided?

What can be discarded?

What is the difference between source material and working state?

These are irritating questions. They slow you down. They make you admit that "include everything" was not thoroughness. It was fear wearing a clever hat.

But the knife is the work.

Summary is not a downgrade from thought. Good summary is thought. Distillation is not what happens after the thinking is done. It is one of the ways thinking happens.

This is the thing large context lets us forget. It makes it possible to keep moving without synthesizing. You can always paste one more thing. You can always add the missing thread. You can always give the model "just a little more background" before forcing yourself to say what you actually believe.

More context did not make me more thoughtful. It made me less willing to choose.

That is the uncomfortable version.

<hr>

To be clear, this is not an anti-long-context argument.

Long context is useful. Sometimes it is miraculous. If you are exploring a codebase, comparing source documents, analyzing transcripts, or letting a model hold a messy research corpus while you ask local questions, large windows can feel like cheating in the best way.

The problem is not the size.

The problem is the lack of structure.

Large context works when paired with structured cognition. Small context helps because it forces structured cognition. The enemy is not context. The enemy is unsynthesized context pretending to be understanding.

The workflow I keep coming back to is boring and therefore probably correct:

Use large context for ingestion and exploration.

Distill aggressively.

Work from the distillate.

Keep the sources available, but do not confuse them with state.

This sounds obvious until you watch how people actually use these systems, myself included. We upload the sources and then keep working inside the soup. The soup gets bigger. The model gets more accommodating. The human gets less precise.

Then we call the output "deep."

Sometimes it is.

Sometimes it is just wet.

<hr>

There is a reason people resist distillation.

Distillation is lossy, and loss feels dangerous. What if you cut the wrong thing? What if the nuance mattered? What if the model needed that weird paragraph from page 47? What if the aside was the key?

These are real risks.

But refusing to lose anything is also a loss. You lose hierarchy. You lose salience. You lose the ability to tell the model what kind of object it is holding. Everything becomes potentially relevant, which is another way of saying nothing is actually prioritized.

The mature move is not to avoid loss.

It is to choose your losses deliberately.

A good distillation does not preserve everything. It preserves the frame, the vocabulary, the decisions, the open tensions, and the evidence that actually bears weight. It leaves behind the parts that can be reloaded if needed but do not need to live in working memory.

This is the same distinction as notes versus state.

Notes are archive.

State is what the next thought needs in order to continue.

Most context-window maximalism is archive envy masquerading as state management.

<hr>

This is also why the dream of "infinite context" feels slightly cursed.

Infinite context sounds like the end of forgetting. But forgetting is not only a bug. Forgetting is one of the ways a system stays oriented. If every past branch remains equally present, the current task has to compete with all its ghosts.

Humans forget badly, obviously. We lose important things. We remember emotionally convenient lies. We reconstruct ourselves with all the reliability of a startup pitch deck.

Still, human forgetting has one accidental virtue: it compresses. The details fade. The shape remains. You remember the fight, not every sentence. You remember the argument, not every tab. You remember the decision, not the entire messy path that produced it.

AI systems need a better version of that.

Not total recall.

Disciplined forgetting.

The point of a harness is not to remember everything. It is to make the system forget correctly.

<hr>

This loops back to `Goldilocks`.

The right context window is not the largest one you can access. It is the one that supports the kind of thinking you are doing without letting you abdicate synthesis.

If you are ingesting, go large.

If you are deciding, go distilled.

If you are drafting, keep the frame close and the archive nearby.

If you are lost, adding more context may be exactly the wrong move. You may not need more material. You may need to say the question out loud.

The adult move is not pretending smaller context is always better. That is just asceticism with a tokenizer.

The adult move is knowing when the hunger for more context is actually fear of making the cut.

<hr>

I still like big context windows.

Of course I do. I am not made of discipline. Give me a tool that says "drop everything here" and some part of me will always relax. The promise is too good: no more forgetting, no more handoff anxiety, no more deciding what matters before I am ready.

But I trust that relaxation less now.

Sometimes it means the tool is genuinely giving me room to think.

Sometimes it means I have found a more technologically impressive way to avoid thinking.

Having everything in context is not the same as knowing what to do next.

