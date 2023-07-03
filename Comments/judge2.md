# Judge 2 - Comments
## General Comments
1. What is less clear to me is that candidate’s individual contribution to the research; this is especially the case with respect to the (arxiv 2022) paper, which has seven co-authors, although all works appear to have alphabetical author order, indicating substantially equivalent contributions.
2. The current form of the thesis is largely inaccessible to anyone not working specifically in differentially private learning. The learning content does not appear to be expressed with enough background to make sense to a person working in differential privacy, and the differential privacy content seems to be treated too superficially to be properly internalized by someone with only a learning background.
3. It is extremely difficult to tease out the nature and significance of the thesis contributions from the introduction, in its current form. The introduction should be written with broad enough language to be accessible to anyone with a reasonable background in theoretical computer science. In my view, it should not have verbose theorems or precise formulae beyond what is absolutely necessary to convey the high-level significance of the work.
4. The literature review reads like it was largely concatenated from the corresponding sections of the papers that compose the thesis. Instead, this review should also attempt to put the work and its significance into context within the broader field in a coherent narrative.
5. I have a similar concern about the background and preliminaries. They are largely irrelevant to the person who is already familiar with the background of the thesis, and completely insufficient for anyone else. I suggest that this section be significantly strengthened to walk a person with basic understanding of learning or differential privacy through the significant results needed to understand the remainder of the thesis. In my view, PhD theses should be self-contained and largely accessible to people interested in more deeply understanding the research area.
6. Consider adding conclusions with a discussion of the limitations of the current works and the important problems left to consider.

## Specific Comments
1. Subsections in the introduction are numbered 1.1, 1.3, and 1.6, with bizarre ordering for sub-subsections. 
2. There is a “Question 1.2”, but what happened to Question 1.1 or Question 1.3? Why are some questions not numbered?
3. Make a habit of not using terms before they are defined (e.g., Theorem 1.2.1, “consistency”, “REC_d^X” – what is the relationship between X and domain X).
4. What is informal about Theorem 1.7.5, page 15 ... could you make it even more
informal, please, for an introduction?
5. Please provide simple examples of important concepts to help make the thesis more broadly accessible. Concepts like VC-dimension, fat shattering dimension, etc. afford simple examples that would help with readability.
6. Please provide simple, high-level explanations for pseudocode (e.g., Algorithm 2 MedBoost, p. 38).
7. Please provide simple, high-level explanations for important concepts (e.g., axis aligned rectangles, p. 56).

