<!-- red = #f8312e -->
<!-- green = #00d369 -->
<!-- orange = #ffb02f -->
<!-- blue = #00a5ed -->
<!-- 🟥🟩🟨🟦 -->

# <span style="font-size:27px; font-family:'Comic Sans MS', cursive"><span style="color:#f8312e">M</span><span style="color:#00d369">a</span><span style="color:#ffb02f">r</span><span style="color:#00a5ed">i</span><span style="color:#00d369">o</span> <span style="color:#00a5ed">B</span><span style="color:#ffb02f">r</span><span style="color:#f8312e">o</span><span style="color:#00d369">s</span> <span style="color:#ffb02f">G</span><span style="color:#f8312e">a</span><span style="color:#00d369">m</span><span style="color:#00a5ed">e</span></span><br />

🟩🟥🟦🟨🟩🟥🟦🟨🟦🟥🟨🟩

<br>

<span style="font-size:20px; font-family:'Comic Sans MS', cursive">A simplifier version fo the famous game Mario Bros with an AI (Reinforcement Learning algorithm && MCTS) that will learn how to complete a custom level of the game.</span>

<br>

# <span style="font-size:27px; font-family:'Comic Sans MS', cursive">Rules</span><br />

🟦🟦🟦🟦

<span style="font-size:20px; font-family:'Comic Sans MS', cursive">Here is an example of a map.</span>

![Game](./assets/game.png)

<span style="font-size:20px; font-family:'Comic Sans MS', cursive">🟦 Player 🟩 Block 🟨 Coin 🟥 Finish</span>

<span style="font-size:20px; font-family:'Comic Sans MS', cursive">The aim of the game is simple: reach the finish line as quickly as possible by collecting the coins.</span>

<span style="font-size:20px; font-family:'Comic Sans MS', cursive">To do this, the player has 2 actions at his disposal :</span>

- <span style="font-size:20px; font-family:'Comic Sans MS', cursive">Go right</span><br />
- <span style="font-size:20px; font-family:'Comic Sans MS', cursive">Jump</span><br />

<br>

## <span style="font-size:22px; font-family:'Comic Sans MS', cursive">Go right</span><br />

🟩🟩🟩🟩🟩

### <span style="font-size:17px; font-family:'Comic Sans MS', cursive">Without block</span><br />

🟨🟨🟨🟨🟨🟨

|       ![Go right without block step 0](./assets/right_without_block0.png)        |       ![Go right without block step 1](./assets/right_without_block1.png)       |
| :------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------: |
| <span style="font-size:17px; font-family:'Comic Sans MS', cursive">Before</span> | <span style="font-size:17px; font-family:'Comic Sans MS', cursive">After</span> |

### <span style="font-size:17px; font-family:'Comic Sans MS', cursive">With block</span><br />

🟨🟨🟨🟨🟨

|          ![Go right with block step 0](./assets/right_with_block0.png)           |          ![Go right with block step 1](./assets/right_with_block1.png)          |
| :------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------: |
| <span style="font-size:17px; font-family:'Comic Sans MS', cursive">Before</span> | <span style="font-size:17px; font-family:'Comic Sans MS', cursive">After</span> |

### <span style="font-size:17px; font-family:'Comic Sans MS', cursive">With hole</span><br />

🟨🟨🟨🟨🟨

|           ![Go right with hole step 0](./assets/right_with_hole0.png)            |           ![Go right with hole step 1](./assets/right_with_hole1.png)           |
| :------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------: |
| <span style="font-size:17px; font-family:'Comic Sans MS', cursive">Before</span> | <span style="font-size:17px; font-family:'Comic Sans MS', cursive">After</span> |

<br>

## <span style="font-size:22px; font-family:'Comic Sans MS', cursive">Jump</span><br />

🟩🟩🟩

### <span style="font-size:17px; font-family:'Comic Sans MS', cursive">Without block</span><br />

🟨🟨🟨🟨🟨🟨

|          ![Jump without block step 0](./assets/jump_without_block0.png)          |        ![Jump without block step 1](./assets/jump_without_block1.png)        |         ![Jump without block step 2](./assets/jump_without_block2.png)          |
| :------------------------------------------------------------------------------: | :--------------------------------------------------------------------------: | :-----------------------------------------------------------------------------: |
| <span style="font-size:17px; font-family:'Comic Sans MS', cursive">Before</span> | <span style="font-size:17px; font-family:'Comic Sans MS', cursive">In</span> | <span style="font-size:17px; font-family:'Comic Sans MS', cursive">After</span> |

### <span style="font-size:17px; font-family:'Comic Sans MS', cursive">With block down</span><br />

🟨🟨🟨🟨🟨🟨🟨🟨

|        ![Jump with block down step 0](./assets/jump_with_block_down0.png)        |      ![Jump with block down step 1](./assets/jump_with_block_down1.png)      |       ![Jump with block down step 2](./assets/jump_with_block_down2.png)        |
| :------------------------------------------------------------------------------: | :--------------------------------------------------------------------------: | :-----------------------------------------------------------------------------: |
| <span style="font-size:17px; font-family:'Comic Sans MS', cursive">Before</span> | <span style="font-size:17px; font-family:'Comic Sans MS', cursive">In</span> | <span style="font-size:17px; font-family:'Comic Sans MS', cursive">After</span> |

### <span style="font-size:17px; font-family:'Comic Sans MS', cursive">With block up</span><br />

🟨🟨🟨🟨🟨🟨

|          ![Jump with block up step 0](./assets/jump_with_block_up0.png)          |        ![Jump with block up step 1](./assets/jump_with_block_up1.png)        |         ![Jump with block up step 2](./assets/jump_with_block_up2.png)          |
| :------------------------------------------------------------------------------: | :--------------------------------------------------------------------------: | :-----------------------------------------------------------------------------: |
| <span style="font-size:17px; font-family:'Comic Sans MS', cursive">Before</span> | <span style="font-size:17px; font-family:'Comic Sans MS', cursive">In</span> | <span style="font-size:17px; font-family:'Comic Sans MS', cursive">After</span> |

### <span style="font-size:17px; font-family:'Comic Sans MS', cursive">Stairway</span><br />

🟨🟨🟨🟨

|          ![Jump with stairway step 0](./assets/jump_with_stairway0.png)          |        ![Jump with stairway step 1](./assets/jump_with_stairway1.png)        |         ![Jump with stairway step 2](./assets/jump_with_stairway2.png)          |
| :------------------------------------------------------------------------------: | :--------------------------------------------------------------------------: | :-----------------------------------------------------------------------------: |
| <span style="font-size:17px; font-family:'Comic Sans MS', cursive">Before</span> | <span style="font-size:17px; font-family:'Comic Sans MS', cursive">In</span> | <span style="font-size:17px; font-family:'Comic Sans MS', cursive">After</span> |

<br>

# <span style="font-size:27px; font-family:'Comic Sans MS', cursive">Gameplay</span><br />

🟦🟦🟦🟦🟦🟦🟦

![Gameplay](./assets/gameplay.gif)

<br>

# <span style="font-size:27px; font-family:'Comic Sans MS', cursive">Report</span><br />

🟦🟦🟦🟦🟦

<span style="font-size:17px; font-family:'Comic Sans MS', cursive">You can find the project report in French [here](https://github.com/H4znow/marioBrossGame/blob/main/report/report.pdf).</span>
