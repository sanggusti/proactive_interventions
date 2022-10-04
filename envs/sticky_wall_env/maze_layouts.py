"""
Maze layouts for ParticleMazeEnv.
Mazes for novel states and changing worlds are adapted from:
    http://www.delorie.com/game-room/mazes/genmaze.cgi
with parameters N=4 and W=H=3. The mazes provided are slightly modified from
the original generated versions in order to reduce local optima. Note that
POLO, AOP, and AOP-BC can do fine in harder mazes.
All mazes should specify a goal, G. A start, S, is optional; if none is
provided, then the agent will spawn randomly. The start is only used at the
beginning of training, or when the agent is stuck in a wall at a world change.
"""

maze_layouts = {
    # Blank mazes for testing
    "blank1": """
+--+--+--+--+
|S          |
|           |
+           +
|           |
|           |
+           +
|           |
|           |
+           +
|           |
|          G|
+--+--+--+--+
""",
    "blank2": """
+--+--+--+--+
|G          |
|           |
+           +
|           |
|           |
+           +
|           |
|           |
+           +
|           |
|          S|
+--+--+--+--+
""",
    "blank3": """
+--+--+--+--+
|          S|
|           |
+           +
|           |
|           |
+           +
|           |
|           |
+           +
|           |
|G          |
+--+--+--+--+
""",
    "blank4": """
+--+--+--+--+
|          G|
|           |
+           +
|           |
|           |
+           +
|           |
|           |
+           +
|           |
|S          |
+--+--+--+--+
""",
    # Novel states mazes
    "novel1": """
+--+--+--+--+
|S |        |
|  |        |
+  +  +--+  +
|     |     |
|     |     |
+  +  +  +  +
|  |     |  |
|  |     |  |
+  +  +  +  +
|     |     |
|     |    G|
+--+--+--+--+
""",
    "novel2": """
+--+--+--+--+
|G |        |
|  |        |
+  +  +--+  +
|     |     |
|     |     |
+  +  +  +  +
|  |     |  |
|  |     |  |
+  +  +  +  +
|     |     |
|     |    S|
+--+--+--+--+
""",
    "novel3": """
+--+--+--+--+
|  |       S|
|  |        |
+  +  +--+  +
|     |     |
|     |     |
+  +  +  +  +
|  |     |  |
|  |     |  |
+  +  +  +  +
|     |     |
|G    |     |
+--+--+--+--+
""",
    "novel4": """
+--+--+--+--+
|  |       G|
|  |        |
+  +  +--+  +
|     |     |
|     |     |
+  +  +  +  +
|  |     |  |
|  |     |  |
+  +  +  +  +
|     |     |
|S    |     |
+--+--+--+--+
""",
    # Changing world mazes
    "1": """
+--+--+--+--+
|S |        |
|  |        |
+  +  +--+  +
|     |     |
|     |     |
+--+  +  +--+
|  |     |  |
|  |     |  |
+  +  +  +  +
|     |     |
|     |    G|
+--+--+--+--+
""",
    "2": """
+--+--+--+--+
|G |        |
|  |        |
+  +  +  +  +
|     |  |  |
|     |  |  |
+  +--+  +  +
|           |
|           |
+  +--+--+  +
|           |
|          S|
+--+--+--+--+
""",
    "3": """
+--+--+--+--+
|S    |     |
|     |     |
+  +--+--+  +
|           |
|           |
+  +--+  +--+
|        |  |
|        |  |
+--+--+  +  +
|           |
|          G|
+--+--+--+--+
""",
    "4": """
+--+--+--+--+
|G    |     |
|     |     |
+  +  +  +  +
|  |     |  |
|  |     |  |
+--+  +  +  +
|     |  |  |
|     |  |  |
+  +--+  +  +
|           |
|          S|
+--+--+--+--+
""",
    "5": """
+--+--+--+--+
|S          |
|           |
+  +--+--+  +
|     |     |
|     |     |
+  +  +  +--+
|  |     |  |
|  |     |  |
+  +  +--+  +
|           |
|          G|
+--+--+--+--+
""",
    "6": """
+--+--+--+--+
|G          |
|           |
+--+  +--+--+
|           |
|           |
+  +--+  +--+
|     |     |
|     |     |
+  +  +--+  +
|  |        |
|  |       S|
+--+--+--+--+
""",
    "7": """
+--+--+--+--+
|S |     |  |
|  |     |  |
+  +--+  +  +
|        |  |
|        |  |
+--+--+  +  +
|     |     |
|     |     |
+  +  +  +  +
|  |     |  |
|  |     | G|
+--+--+--+--+
""",
    "8": """
+--+--+--+--+
|G |     |  |
|  |     |  |
+  +  +  +  +
|     |     |
|     |     |
+  +--+  +  +
|     |  |  |
|     |  |  |
+  +  +  +  +
|  |        |
|  |       S|
+--+--+--+--+
""",
    "9": """
+--+--+--+--+
|S          |
|           |
+  +--+--+  +
|     |     |
|     |     |
+--+  +  +--+
|  |     |  |
|  |     |  |
+  +  +  +  +
|     |     |
|     |    G|
+--+--+--+--+
""",
    "10": """
+--+--+--+--+
|G          |
|           |
+  +  +  +  +
|  |  |  |  |
|  |  |  |  |
+  +--+  +  +
|  |        |
|  |        |
+  +  +--+  +
|     |     |
|     |    S|
+--+--+--+--+
""",
    "11": """
+--+--+--+--+
|S       |  |
|        |  |
+--+  +--+  +
|           |
|           |
+  +--+--+  +
|        |  |
|        |  |
+--+  +  +  +
|     |     |
|     |    G|
+--+--+--+--+
""",
    "12": """
+--+--+--+--+
|G |     |  |
|  |     |  |
+  +  +  +  +
|  |  |  |  |
|  |  |  |  |
+  +--+  +  +
|     |  |  |
|     |  |  |
+  +  +  +  +
|  |        |
|  |       S|
+--+--+--+--+
""",
    "13": """
+--+--+--+--+
|S    |     |
|     |     |
+--+  +  +  +
|        |  |
|        |  |
+  +--+  +  +
|     |  |  |
|     |  |  |
+--+  +  +  +
|     |     |
|     |    G|
+--+--+--+--+
""",
    "14": """
+--+--+--+--+
|G |        |
|  |        |
+  +  +--+  +
|     |     |
|     |     |
+  +  +  +--+
|  |  |  |  |
|  |  |  |  |
+  +  +  +  +
|  |        |
|  |       S|
+--+--+--+--+
""",
    "15": """
+--+--+--+--+
|S          |
|           |
+  +--+--+  +
|        |  |
|        |  |
+--+  +--+  +
|           |
|           |
+--+--+  +--+
|           |
|          G|
+--+--+--+--+
""",
    "16": """
+--+--+--+--+
|G    |     |
|     |     |
+  +  +--+  +
|  |        |
|  |        |
+  +--+  +--+
|  |        |
|  |        |
+--+  +  +--+
|     |     |
|     |    S|
+--+--+--+--+
""",
    "17": """
+--+--+--+--+
|S          |
|           |
+  +--+--+  +
|        |  |
|        |  |
+--+--+  +  +
|     |     |
|     |     |
+  +--+--+  +
|           |
|          G|
+--+--+--+--+
""",
    "18": """
+--+--+--+--+
|G |        |
|  |        |
+  +--+  +  +
|  |     |  |
|  |     |  |
+  +--+  +  +
|        |  |
|        |  |
+--+  +--+  +
|           |
|          S|
+--+--+--+--+
""",
    "19": """
+--+--+--+--+
|S          |
|           |
+--+  +  +--+
|     |     |
|     |     |
+  +--+--+  +
|  |        |
|  |        |
+  +  +--+  +
|     |     |
|     |    G|
+--+--+--+--+
""",
    "20": """
+--+--+--+--+
|G          |
|           |
+--+  +--+  +
|  |     |  |
|  |     |  |
+  +--+  +  +
|  |     |  |
|  |     |  |
+  +  +  +  +
|     |     |
|     |    S|
+--+--+--+--+
""",
    "21": """
+--+--+--+--+
|S          |
|           |
+  +--+  +--+
|  |        |
|  |        |
+  +--+  +--+
|  |        |
|  |        |
+  +  +--+  +
|     |     |
|     |    G|
+--+--+--+--+
""",
    "22": """
+--+--+--+--+
|G          |
|           |
+  +  +--+  +
|  |  |     |
|  |  |     |
+  +  +  +  +
|  |     |  |
|  |     |  |
+  +--+  +  +
|           |
|          S|
+--+--+--+--+
""",
    "23": """
+--+--+--+--+
|S       |  |
|        |  |
+--+--+  +  +
|           |
|           |
+  +--+  +--+
|  |  |     |
|  |  |     |
+  +  +  +  +
|        |  |
|        | G|
+--+--+--+--+
""",
    "24": """
+--+--+--+--+
|G    |     |
|     |     |
+  +  +--+  +
|  |        |
|  |        |
+  +  +--+--+
|     |  |  |
|     |  |  |
+--+  +  +  +
|           |
|          S|
+--+--+--+--+
""",
    "25": """
+--+--+--+--+
|S |        |
|  |        |
+  +  +--+  +
|  |     |  |
|  |     |  |
+  +--+  +  +
|        |  |
|        |  |
+  +--+  +  +
|     |     |
|     |    G|
+--+--+--+--+
""",
    "26": """
+--+--+--+--+
|G |        |
|  |        |
+  +  +--+  +
|  |  |     |
|  |  |     |
+  +--+  +  +
|        |  |
|        |  |
+--+  +--+  +
|           |
|          S|
+--+--+--+--+
""",
    "27": """
+--+--+--+--+
|S       |  |
|        |  |
+--+--+  +  +
|     |  |  |
|     |  |  |
+  +--+  +  +
|        |  |
|        |  |
+--+  +  +  +
|     |     |
|     |    G|
+--+--+--+--+
""",
    "28": """
+--+--+--+--+
|G          |
|           |
+  +--+  +  +
|     |  |  |
|     |  |  |
+--+  +  +  +
|     |  |  |
|     |  |  |
+  +--+  +  +
|        |  |
|        | S|
+--+--+--+--+
""",
    "29": """
+--+--+--+--+
|S |     |  |
|  |     |  |
+  +  +--+  +
|           |
|           |
+--+--+  +--+
|           |
|           |
+  +--+--+  +
|     |     |
|     |    G|
+--+--+--+--+
""",
    "30": """
+--+--+--+--+
|G |        |
|  |        |
+  +  +--+  +
|  |        |
|  |        |
+  +--+  +--+
|  |  |  |  |
|  |  |  |  |
+  +  +  +  +
|           |
|          S|
+--+--+--+--+
""",
    "31": """
+--+--+--+--+
|S          |
|           |
+  +  +  +  +
|  |  |  |  |
|  |  |  |  |
+  +--+--+  +
|     |  |  |
|     |  |  |
+--+  +  +  +
|           |
|          G|
+--+--+--+--+
""",
    "32": """
+--+--+--+--+
|G          |
|           |
+  +  +--+  +
|  |  |     |
|  |  |     |
+  +  +--+  +
|     |     |
|     |     |
+  +  +  +--+
|  |        |
|  |       S|
+--+--+--+--+
""",
    "33": """
+--+--+--+--+
|S          |
|           |
+--+--+  +--+
|           |
|           |
+  +  +--+  +
|  |     |  |
|  |     |  |
+  +  +--+--+
|           |
|          G|
+--+--+--+--+
""",
    "34": """
+--+--+--+--+
|G          |
|           |
+  +--+  +  +
|  |  |  |  |
|  |  |  |  |
+  +  +  +--+
|  |        |
|  |        |
+  +  +--+  +
|     |     |
|     |    S|
+--+--+--+--+
""",
    "35": """
+--+--+--+--+
|S       |  |
|        |  |
+--+  +--+  +
|           |
|           |
+  +--+--+  +
|  |  |     |
|  |  |     |
+  +  +  +  +
|        |  |
|        | G|
+--+--+--+--+
""",
    "36": """
+--+--+--+--+
|G    |     |
|     |     |
+--+  +  +  +
|        |  |
|        |  |
+  +--+--+  +
|        |  |
|        |  |
+--+  +  +  +
|     |     |
|     |    S|
+--+--+--+--+
""",
    "37": """
+--+--+--+--+
|S |        |
|  |        |
+  +  +--+  +
|  |  |     |
|  |  |     |
+  +  +  +--+
|           |
|           |
+--+--+--+  +
|           |
|          G|
+--+--+--+--+
""",
    "38": """
+--+--+--+--+
|G          |
|           |
+  +--+  +--+
|  |        |
|  |        |
+  +--+--+  +
|     |     |
|     |     |
+--+  +  +  +
|        |  |
|        | S|
+--+--+--+--+
""",
    "39": """
+--+--+--+--+
|S    |     |
|     |     |
+  +  +--+  +
|  |        |
|  |        |
+  +--+  +--+
|  |     |  |
|  |     |  |
+  +  +  +  +
|     |     |
|     |    G|
+--+--+--+--+
""",
    "40": """
+--+--+--+--+
|G    |     |
|     |     |
+  +  +  +  +
|  |     |  |
|  |     |  |
+  +  +  +  +
|     |  |  |
|     |  |  |
+  +  +  +  +
|  |        |
|  |       S|
+--+--+--+--+
""",
    "41": """
+--+--+--+--+
|S |        |
|  |        |
+  +  +--+  +
|     |  |  |
|     |  |  |
+  +--+  +  +
|        |  |
|        |  |
+  +  +  +  +
|  |  |     |
|  |  |    G|
+--+--+--+--+
""",
    "42": """
+--+--+--+--+
|G    |     |
|     |     |
+--+  +  +--+
|           |
|           |
+  +--+--+--+
|           |
|           |
+--+  +--+  +
|     |     |
|     |    S|
+--+--+--+--+
""",
    "43": """
+--+--+--+--+
|S       |  |
|        |  |
+--+  +  +  +
|     |     |
|     |     |
+--+  +--+  +
|           |
|           |
+--+  +  +--+
|     |     |
|     |    G|
+--+--+--+--+
""",
    "44": """
+--+--+--+--+
|G |        |
|  |        |
+  +  +--+  +
|     |     |
|     |     |
+  +--+  +--+
|           |
|           |
+  +  +--+  +
|  |        |
|  |       S|
+--+--+--+--+
""",
    "45": """
+--+--+--+--+
|S       |  |
|        |  |
+  +--+  +  +
|  |  |  |  |
|  |  |  |  |
+--+  +  +  +
|     |     |
|     |     |
+  +  +--+  +
|  |        |
|  |       G|
+--+--+--+--+
""",
    "46": """
+--+--+--+--+
|G          |
|           |
+  +--+  +--+
|  |        |
|  |        |
+--+  +--+--+
|     |     |
|     |     |
+--+  +  +  +
|        |  |
|        | S|
+--+--+--+--+
""",
    "47": """
+--+--+--+--+
|S    |     |
|     |     |
+--+  +  +  +
|  |     |  |
|  |     |  |
+  +--+  +  +
|  |     |  |
|  |     |  |
+  +  +  +  +
|     |     |
|     |    G|
+--+--+--+--+
""",
    "48": """
+--+--+--+--+
|G |     |  |
|  |     |  |
+  +  +  +  +
|     |     |
|     |     |
+  +--+  +  +
|        |  |
|        |  |
+--+  +--+  +
|           |
|          S|
+--+--+--+--+
""",
    "49": """
+--+--+--+--+
|S |     |  |
|  |     |  |
+  +  +  +  +
|  |  |     |
|  |  |     |
+  +--+--+  +
|     |     |
|     |     |
+--+  +  +  +
|        |  |
|        | G|
+--+--+--+--+
""",
    "50": """
+--+--+--+--+
|G    |     |
|     |     |
+--+  +  +--+
|     |     |
|     |     |
+  +--+  +  +
|        |  |
|        |  |
+--+--+  +  +
|        |  |
|        | S|
+--+--+--+--+
""",
    "51": """
+--+--+--+--+
|S |        |
|  |        |
+  +--+  +  +
|        |  |
|        |  |
+--+  +--+  +
|           |
|           |
+  +--+  +--+
|           |
|          G|
+--+--+--+--+
""",
    "52": """
+--+--+--+--+
|G       |  |
|        |  |
+  +--+  +  +
|  |        |
|  |        |
+  +  +--+  +
|     |     |
|     |     |
+  +--+  +--+
|           |
|          S|
+--+--+--+--+
""",
    "53": """
+--+--+--+--+
|S    |     |
|     |     |
+--+  +  +  +
|        |  |
|        |  |
+  +--+  +  +
|  |        |
|  |        |
+  +  +--+--+
|           |
|          G|
+--+--+--+--+
""",
    "54": """
+--+--+--+--+
|G       |  |
|        |  |
+  +  +  +  +
|  |  |     |
|  |  |     |
+  +  +--+  +
|           |
|           |
+  +--+  +  +
|        |  |
|        | S|
+--+--+--+--+
""",
    "55": """
+--+--+--+--+
|S |        |
|  |        |
+  +  +--+  +
|           |
|           |
+  +--+  +  +
|  |     |  |
|  |     |  |
+  +  +  +  +
|     |     |
|     |    G|
+--+--+--+--+
""",
    "56": """
+--+--+--+--+
|G          |
|           |
+--+  +  +  +
|     |  |  |
|     |  |  |
+  +  +  +  +
|  |     |  |
|  |     |  |
+  +--+--+  +
|           |
|          S|
+--+--+--+--+
""",
    "57": """
+--+--+--+--+
|S       |  |
|        |  |
+  +--+  +  +
|     |     |
|     |     |
+  +  +--+  +
|  |        |
|  |        |
+  +--+--+  +
|           |
|          G|
+--+--+--+--+
""",
    "58": """
+--+--+--+--+
|G       |  |
|        |  |
+--+  +  +  +
|     |     |
|     |     |
+  +  +  +  +
|  |  |  |  |
|  |  |  |  |
+  +--+  +  +
|           |
|          S|
+--+--+--+--+
""",
    "59": """
+--+--+--+--+
|S    |     |
|     |     |
+--+  +     +
|           |
|           |
+  +--+--+  +
|           |
|           |
+  +  +  +--+
|  |  |     |
|  |  |    G|
+--+--+--+--+
""",
    "60": """
+--+--+--+--+
|G |     |  |
|  |     |  |
+  +--+  +  +
|           |
|           |
+--+  +  +--+
|     |  |  |
|     |  |  |
+  +--+  +  +
|           |
|          S|
+--+--+--+--+
""",
    "61": """
+--+--+--+--+
|S       |  |
|        |  |
+  +--+  +  +
|           |
|           |
+  +--+  +--+
|     |  |  |
|     |  |  |
+--+  +  +  +
|           |
|          G|
+--+--+--+--+
""",
    "62": """
+--+--+--+--+
|G          |
|           |
+  +  +--+  +
|  |  |     |
|  |  |     |
+--+  +  +--+
|     |     |
|     |     |
+  +--+  +  +
|        |  |
|        | S|
+--+--+--+--+
""",
    "63": """
+--+--+--+--+
|S          |
|           |
+--+--+  +--+
|           |
|           |
+  +--+  +--+
|           |
|           |
+--+--+  +  +
|        |  |
|        | G|
+--+--+--+--+
""",
    "64": """
+--+--+--+--+
|G |        |
|  |        |
+  +  +  +  +
|     |  |  |
|     |  |  |
+--+  +--+  +
|     |     |
|     |     |
+  +  +  +--+
|  |        |
|  |       S|
+--+--+--+--+
""",
    "65": """
+--+--+--+--+
|S          |
|           |
+--+  +--+  +
|     |     |
|     |     |
+  +--+--+  +
|  |        |
|  |        |
+  +  +--+  +
|     |     |
|     |    G|
+--+--+--+--+
""",
    "66": """
+--+--+--+--+
|G          |
|           |
+--+  +  +  +
|     |  |  |
|     |  |  |
+  +--+  +  +
|        |  |
|        |  |
+  +--+--+  +
|           |
|          S|
+--+--+--+--+
""",
    "67": """
+--+--+--+--+
|S       |  |
|        |  |
+  +--+  +  +
|  |  |     |
|  |  |     |
+  +  +--+  +
|        |  |
|        |  |
+--+  +--+  +
|           |
|          G|
+--+--+--+--+
""",
    "68": """
+--+--+--+--+
|G          |
|           |
+  +--+--+  +
|           |
|           |
+--+  +  +--+
|     |     |
|     |     |
+  +--+--+  +
|           |
|          S|
+--+--+--+--+
""",
    "69": """
+--+--+--+--+
|S    |     |
|     |     |
+  +  +  +  +
|  |     |  |
|  |     |  |
+--+  +--+  +
|           |
|           |
+  +--+--+  +
|           |
|          G|
+--+--+--+--+
""",
    "70": """
+--+--+--+--+
|G |     |  |
|  |     |  |
+  +  +  +  +
|     |     |
|     |     |
+--+  +--+  +
|  |        |
|  |        |
+  +  +--+--+
|           |
|          S|
+--+--+--+--+
""",
    "71": """
+--+--+--+--+
|S          |
|           |
+--+  +  +--+
|     |     |
|     |     |
+  +--+--+  +
|  |        |
|  |        |
+  +--+--+  +
|           |
|          G|
+--+--+--+--+
""",
    "72": """
+--+--+--+--+
|G |     |  |
|  |     |  |
+  +  +  +  +
|     |     |
|     |     |
+--+  +--+  +
|  |  |     |
|  |  |     |
+  +  +  +--+
|           |
|          S|
+--+--+--+--+
""",
    "73": """
+--+--+--+--+
|S    |  |  |
|     |  |  |
+  +--+  +  +
|     |  |  |
|     |  |  |
+  +--+  +  +
|     |     |
|     |     |
+--+  +  +--+
|           |
|          G|
+--+--+--+--+
""",
    "74": """
+--+--+--+--+
|G          |
|           |
+--+  +--+  +
|     |     |
|     |     |
+  +--+  +--+
|  |     |  |
|  |     |  |
+  +  +--+  +
|           |
|          S|
+--+--+--+--+
""",
    "75": """
+--+--+--+--+
|S          |
|           |
+--+  +--+  +
|  |  |     |
|  |  |     |
+  +  +  +--+
|  |  |  |  |
|  |  |  |  |
+  +  +  +  +
|           |
|          G|
+--+--+--+--+
""",
    "76": """
+--+--+--+--+
|G    |     |
|     |     |
+  +  +--+  +
|  |        |
|  |        |
+  +--+--+  +
|     |     |
|     |     |
+--+  +  +--+
|     |     |
|     |    S|
+--+--+--+--+
""",
    "77": """
+--+--+--+--+
|S    |     |
|     |     |
+--+  +  +  +
|     |  |  |
|     |  |  |
+  +--+--+  +
|        |  |
|        |  |
+--+  +  +  +
|     |     |
|     |    G|
+--+--+--+--+
""",
    "78": """
+--+--+--+--+
|G          |
|           |
+  +--+--+  +
|        |  |
|        |  |
+  +--+  +  +
|     |  |  |
|     |  |  |
+--+  +  +  +
|     |     |
|     |    S|
+--+--+--+--+
""",
    "79": """
+--+--+--+--+
|S          |
|           |
+  +--+  +  +
|  |     |  |
|  |     |  |
+--+--+--+  +
|           |
|           |
+--+--+  +  +
|        |  |
|        | G|
+--+--+--+--+
""",
    "80": """
+--+--+--+--+
|G |        |
|  |        |
+  +  +  +  +
|     |  |  |
|     |  |  |
+--+--+  +  +
|        |  |
|        |  |
+  +--+--+  +
|           |
|          S|
+--+--+--+--+
""",
    "81": """
+--+--+--+--+
|S |        |
|  |        |
+  +--+  +  +
|        |  |
|        |  |
+  +--+--+  +
|  |     |  |
|  |     |  |
+  +  +  +  +
|     |     |
|     |    G|
+--+--+--+--+
""",
    "82": """
+--+--+--+--+
|G    |     |
|     |     |
+--+  +  +--+
|     |     |
|     |     |
+  +  +  +  +
|  |     |  |
|  |     |  |
+  +--+--+  +
|           |
|          S|
+--+--+--+--+
""",
    "83": """
+--+--+--+--+
|S          |
|           |
+--+--+--+  +
|  |        |
|  |        |
+  +  +--+  +
|        |  |
|        |  |
+  +--+--+  +
|        |  |
|        | G|
+--+--+--+--+
""",
    "84": """
+--+--+--+--+
|G          |
|           |
+  +--+--+  +
|        |  |
|        |  |
+--+--+  +  +
|     |  |  |
|     |  |  |
+  +  +  +  +
|  |     |  |
|  |     | S|
+--+--+--+--+
""",
    "85": """
+--+--+--+--+
|S |     |  |
|  |     |  |
+  +--+  +  +
|  |     |  |
|  |     |  |
+  +  +--+  +
|  |        |
|  |        |
+  +  +  +--+
|     |     |
|     |    G|
+--+--+--+--+
""",
    "86": """
+--+--+--+--+
|G          |
|           |
+  +--+  +  +
|     |  |  |
|     |  |  |
+--+  +  +  +
|     |  |  |
|     |  |  |
+  +--+--+  +
|           |
|          S|
+--+--+--+--+
""",
    "87": """
+--+--+--+--+
|S          |
|           |
+--+--+  +--+
|  |        |
|  |        |
+  +  +  +  +
|     |  |  |
|     |  |  |
+  +--+--+  +
|           |
|          G|
+--+--+--+--+
""",
    "88": """
+--+--+--+--+
|G |        |
|  |        |
+  +  +--+  +
|     |     |
|     |     |
+  +  +  +--+
|  |  |  |  |
|  |  |  |  |
+  +--+  +  +
|     |     |
|     |    S|
+--+--+--+--+
""",
    "89": """
+--+--+--+--+
|S          |
|           |
+--+  +--+  +
|     |     |
|     |     |
+--+  +  +--+
|     |     |
|     |     |
+  +--+--+  +
|           |
|          G|
+--+--+--+--+
""",
    "90": """
+--+--+--+--+
|G |        |
|  |        |
+  +--+  +  +
|        |  |
|        |  |
+--+  +--+  +
|        |  |
|        |  |
+  +--+--+  +
|           |
|          S|
+--+--+--+--+
""",
    "91": """
+--+--+--+--+
|S          |
|           |
+  +--+--+  +
|           |
|           |
+  +--+  +--+
|  |     |  |
|  |     |  |
+  +  +  +  +
|     |     |
|     |    G|
+--+--+--+--+
""",
    "92": """
+--+--+--+--+
|G    |     |
|     |     |
+--+  +  +  +
|        |  |
|        |  |
+  +--+--+  +
|     |     |
|     |     |
+  +--+--+  +
|           |
|          S|
+--+--+--+--+
""",
    "93": """
+--+--+--+--+
|S    |  |  |
|     |  |  |
+--+  +  +  +
|           |
|           |
+  +--+  +  +
|  |  |  |  |
|  |  |  |  |
+  +  +  +  +
|        |  |
|        | G|
+--+--+--+--+
""",
    "94": """
+--+--+--+--+
|G          |
|           |
+  +--+--+  +
|           |
|           |
+  +--+--+  +
|        |  |
|        |  |
+--+  +  +  +
|     |     |
|     |    S|
+--+--+--+--+
""",
    "95": """
+--+--+--+--+
|S          |
|           |
+--+  +--+  +
|  |        |
|  |        |
+  +  +  +  +
|     |  |  |
|     |  |  |
+--+  +--+  +
|           |
|          G|
+--+--+--+--+
""",
    "96": """
+--+--+--+--+
|G          |
|           |
+  +--+--+  +
|           |
|           |
+  +--+--+--+
|  |     |  |
|  |     |  |
+  +  +  +  +
|     |     |
|     |    S|
+--+--+--+--+
""",
    "97": """
+--+--+--+--+
|S          |
|           |
+--+--+--+  +
|  |        |
|  |        |
+  +--+  +--+
|           |
|           |
+--+  +--+  +
|     |     |
|     |    G|
+--+--+--+--+
""",
    "98": """
+--+--+--+--+
|G    |     |
|     |     |
+  +  +  +--+
|  |  |     |
|  |  |     |
+  +  +--+  +
|     |     |
|     |     |
+  +--+  +  +
|        |  |
|        | S|
+--+--+--+--+
""",
    "99": """
+--+--+--+--+
|S    |     |
|     |     |
+--+  +--+  +
|  |  |     |
|  |  |     |
+  +  +  +  +
|  |     |  |
|  |     |  |
+  +--+--+  +
|           |
|          G|
+--+--+--+--+
""",
    "100": """
+--+--+--+--+
|G          |
|           |
+--+  +--+  +
|     |     |
|     |     |
+  +--+  +  +
|  |     |  |
|  |     |  |
+  +  +  +  +
|     |     |
|     |    S|
+--+--+--+--+
""",
    # Initial state
    "init-1A": """
+--+--+--+--+
|           |
|           |
+--+ S+--+  +
|     |     |
|     |     |
+  +--+  +  +
|  |     |  |
|  |     |  |
+  +  +--+  +
|           |
|          G|
+--+--+--+--+
""",
    "init-1B": """
+--+--+--+--+
|S          |
|           |
+--+  +--+  +
|     |     |
|     |     |
+  +--+  +  +
|  |     |  |
|  |     |  |
+  +  +--+  +
|           |
|          G|
+--+--+--+--+
""",
    "init-2A": """
+--+--+--+--+
|         S |
|           |
+--+  +--+  +
|     |     |
|     |     |
+  +--+  +  +
|  |     |  |
|  |     |  |
+  +  +--+  +
|           |
|          G|
+--+--+--+--+
""",
    "init-2B": """
+--+--+--+--+
|           |
|           |
+--+  +--+  +
|     |     |
|     |     |
+  +--+  +  +
|  |     |  |
|  |     |  |
+  +  +--+  +
|S          |
|          G|
+--+--+--+--+
""",
    "init-3A": """
+--+--+--+--+
|           |
|           |
+--+  +--+  +
|S    |     |
|     |     |
+  +--+  +  +
|  |     |  |
|  |     |  |
+  +  +--+  +
|           |
|          G|
+--+--+--+--+
""",
    "init-3B": """
+--+--+--+--+
|           |
|           |
+--+  +--+  +
|     |     |
|     |     |
+  +--+  +  +
|  |     |  |
|  |     |  |
+  +  +--+  +
|    S      |
|          G|
+--+--+--+--+
""",
    "init-4A": """
+--+--+--+--+
|           |
|           |
+--+  +--+  +
|    S|     |
|     |     |
+  +--+  +  +
|  |     |  |
|  |     |  |
+  +  +--+  +
|           |
|          G|
+--+--+--+--+
""",
    "init-4B": """
+--+--+--+--+
|           |
|           |
+--+  +--+  +
|     |     |
|     |     |
+  +--+  +  +
|  |     |  |
|  |    S|  |
+  +  +--+  +
|           |
|          G|
+--+--+--+--+
""",
    # Walls removed
    "walls-000": """
+--+--+--+--+
|S          |
|           |
+     +--+  +
|           |
|           |
+  +     +--+
|  |        |
|  |        |
+  +  +     +
|     |     |
|     |    G|
+--+--+--+--+
""",
    "walls-001": """
+--+--+--+--+
|S          |
|           |
+     +--+  +
|           |
|           |
+  +     +--+
|  |     |  |
|  |     |  |
+  +  +  +  +
|     |     |
|     |    G|
+--+--+--+--+
""",
    "walls-010": """
+--+--+--+--+
|S          |
|           |
+     +--+  +
|     |     |
|     |     |
+  +  +  +--+
|  |        |
|  |        |
+  +  +     +
|     |     |
|     |    G|
+--+--+--+--+
""",
    "walls-011": """
+--+--+--+--+
|S          |
|           |
+     +--+  +
|     |     |
|     |     |
+  +  +  +--+
|  |     |  |
|  |     |  |
+  +  +  +  +
|     |     |
|     |    G|
+--+--+--+--+
""",
    "walls-100": """
+--+--+--+--+
|S |        |
|  |        |
+  +  +--+  +
|           |
|           |
+  +     +--+
|  |        |
|  |        |
+  +  +     +
|     |     |
|     |    G|
+--+--+--+--+
""",
    "walls-101": """
+--+--+--+--+
|S |        |
|  |        |
+  +  +--+  +
|           |
|           |
+  +     +--+
|  |     |  |
|  |     |  |
+  +  +  +  +
|     |     |
|     |    G|
+--+--+--+--+
""",
    "walls-110": """
+--+--+--+--+
|S |        |
|  |        |
+  +  +--+  +
|     |     |
|     |     |
+  +  +  +--+
|  |        |
|  |        |
+  +  +     +
|     |     |
|     |    G|
+--+--+--+--+
""",
    "walls-111": """
+--+--+--+--+
|S |        |
|  |        |
+  +  +--+  +
|     |     |
|     |     |
+  +  +  +--+
|  |     |  |
|  |     |  |
+  +  +  +  +
|     |     |
|     |    G|
+--+--+--+--+
""",
}