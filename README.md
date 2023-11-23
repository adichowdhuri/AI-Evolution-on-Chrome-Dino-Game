<!DOCTYPE html>
<html>
<body>

<h1>Dino Game with AI</h1>

<h1>Introduction</h1>
<p>This repository hosts a Python-based game that integrates a dinosaur character with Artificial Intelligence (AI) using the NeuroEvolution of Augmenting Topologies (NEAT) algorithm. NEAT is a genetic algorithm that evolves artificial neural networks, allowing the AI to learn and adapt to navigate through obstacles. It starts with simple networks and evolves over generations to produce more complex and efficient solutions, making the AI's learning process both dynamic and efficient. This game offers an engaging platform where the dinosaur learns and adapts to avoid cacti, showcasing the practical application of NEAT in game development.</p>

<h1>Features</h1>
<ul>
    <li><strong>AI-Controlled Dinosaur</strong>: The dinosaur character's movements are managed by an AI agent, learning to avoid obstacles over time.</li>
    <li><strong>Dynamic Obstacles</strong>: The game features randomly generated obstacles like small and large cacti.</li>
    <li><strong>Interactive Graphics</strong>: Developed using the `pygame` library, the game offers engaging visual animations.</li>
    <li><strong>Customizable AI Settings</strong>: AI behavior can be adjusted in the `config.txt` file, allowing for various gameplay strategies.</li>
</ul>

<h1>Repository Structure</h1>
<pre><code>
AI-Evolution-on-Chrome-Dino-Game/
│
├── images/                  # Folder containing all game assets
│
├── Dino.py                  # Chrome Dino game script (no AI)
│
├── DinoAI.py                # Script adding AI into the game
│
├── config.txt               # Parameters for AI configuration
│
├── requirements.txt         # Project dependencies
│
└── README.md                # Project documentation
</code></pre>

<h1>Tech Stack</h1>
<p>The Dino Game with AI is built using a variety of technologies:</p>

| <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" alt="Python Icon" height="80"> | <img src="https://www.pygame.org/docs/_images/pygame_logo.png" alt="Pygame Icon" height="80"> | <img src="https://cdn-icons-png.flaticon.com/512/9304/9304615.png" alt="NEAT Icon" height="80"> |
|:---:|:---:|:---:|
| <strong>Python</strong><br>Primary programming language. | <strong>Pygame</strong><br>Library used for game development. | <strong>NEAT-Python</strong><br>Library for implementing the NEAT algorithm. |

<style>
table, th, td {
  border: none;
}
</style>


<h1>Game Screenshots</h1>
<p>Here are some screenshots showcasing different moments of the game:</p>
<div>
    <img src="https://github.com/adichowdhuri/AI-Evolution-on-Chrome-Dino-Game/assets/96464997/cb0db164-1082-43db-84a7-2f6c5d8fea40" alt="Dino Game Screenshot 2">
    <img src="https://github.com/adichowdhuri/AI-Evolution-on-Chrome-Dino-Game/assets/96464997/3e155356-6369-4fc8-b271-c9c264abf4d0" alt="Dino Game Screenshot 2">
</div>

<h1>NEAT Algorithm</h1>
<p>The NEAT algorithm is a method for evolving artificial neural networks with a genetic algorithm. Here's a simple overview of how it works:</p>
<img src="https://miro.medium.com/v2/resize:fit:875/1*MkFz_fYk2wGHeE-bEe-32w.png" alt="NEAT Algorithm Diagram">
<h1>Installation and Setup</h1>
<h2>Cloning the Repository</h2>
<ol>
    <li><strong>Open a Terminal or Command Prompt</strong>:
        <ul>
            <li>Run the following command:
                <pre><code>git clone https://github.com/adichowdhuri/AI-Evolution-on-Chrome-Dino-Game.git</code></pre>
            </li>
        </ul>
    </li>
</ol>

<h2>Installing Dependencies</h2>
<ol>
    <li><strong>Navigate to the Repository Directory</strong>:
        <ul>
            <li>Change to the cloned repository's directory:
                <pre><code>cd AI-Evolution-on-Chrome-Dino-Game</code></pre>
            </li>
        </ul>
    </li>
    <li><strong>Install Project Dependencies</strong>:
        <ul>
            <li>Run:
                <pre><code>pip install -r requirements.txt</code></pre>
            </li>
        </ul>
    </li>
</ol>

<h1>Usage</h1>
<p>To start the game, execute the <code>Dino.py</code> script in the project directory. The AI will begin learning to navigate through the obstacles. Here's how you can run the game:</p>
<pre><code>python DinoAI.py</code></pre>
<p>Watch the dinosaur as it tries different strategies to avoid cacti. Over time, you'll notice the AI improving its obstacle avoidance tactics.</p>

<h1>Customizing AI Behavior</h1>
<p>To customize the AI behavior, modify the settings in the <code>config.txt</code> file. This file contains various parameters that control the AI's learning process. For example, you can change the mutation rate or the number of generations. Here's a sample configuration:</p>
<pre><code>
[NEAT]
pop_size = 50
fitness_criterion = max
fitness_threshold = 1000
...
</code></pre>

<h1>Customizing AI Behavior</h1>
<p>Modify the <code>config.txt</code> file to experiment with different AI learning parameters and behaviors.</p>

<h2>Contributing</h2>
<p>Contributions to enhance or improve the game are welcome. Please fork the repository and submit pull requests with your changes.</p>

<h1>License</h1>
<p>This project is open-sourced under the MIT License. For more details, see the <a href="https://github.com/adichowdhuri/AI-Evolution-on-Chrome-Dino-Game/blob/main/LICENSE">license file</a>.</p>

<h1>Acknowledgements</h1>
<p>Special thanks to the open-source community for their invaluable resources and support.</p>

</body>
</html>
