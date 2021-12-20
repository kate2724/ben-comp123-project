import sys
import tkinter as tk


# the basic idea is we can put tags on different parts of the text, and some of those tags can do things if we
# click on them, like deleting all the existing text and inserting more. text tagged with a number does the
# click_link for that number
class App:
    def __init__(self, master):
        # creates the window, text box, etc...
        self.master = master
        self.master.config(background="#000000")
        self.frame = tk.Frame(self.master)
        self.frame.config(relief=tk.FLAT, background="#2b2b2b")
        self.frame.pack(expand=True)
        self.text = tk.Text(self.frame, background="#2b2b2b", foreground="#A9B7C6", cursor="arrow",
                            relief=tk.FLAT, padx=0, pady=0, width=80, height=25, wrap=tk.WORD)
        self.exit = tk.Text(self.frame, background="#2b2b2b", foreground="#94558d", cursor="hand2",
                            relief=tk.FLAT, padx=0, pady=0, width=4, height=1)

        # starting text
        self.text.insert('1.0', "start", (0, "magenta", "cursor"))
        self.text.config(state=tk.DISABLED)
        self.exit.insert("1.0", "exit", 0)
        self.exit.config(state=tk.DISABLED)
        self.text.pack()
        self.exit.pack(anchor="e")

        # creates a hyperlink bind for each of the keys, associated with the corresponding tag
        keys = range(1000)
        for tag in keys:
            self.text.tag_bind(tag, "<1>", lambda event, key=tag: self.click_link(event, key))

        # gives functionality to the exit button
        self.exit.tag_bind(0, "<1>", lambda _: sys.exit())

        # some colours
        self.text.tag_config('magenta', foreground="#94558d")
        self.text.tag_config("red", foreground="#C75450")
        self.text.tag_config('blue', foreground="#589DF6")

        # changes the cursor when it hovers over text tagged with "cursor"
        self.text.tag_bind("cursor", "<Enter>", lambda event: self.text.config(cursor="hand2"))
        self.text.tag_bind("cursor", "<Leave>", lambda event: self.text.config(cursor="arrow"))

        # a few variables to help with the electrostatics storyline
        self.devil = False                          # if letter d needs to be removed
        self.poem = False                           # if we need to be able to type
        self.major = "Ancient Japanese History"     # name of major, defaults to japanese history if undeclared
        self.estatics = 0                           # which chapter of the storyline we are in
        self.major2 = False                         # if we have declared major yet

    def click_link(self, event, key):
        """gets a key from the hyperlink and then does the corresponding actions"""
        if key == 0:
            self.rewrite(
                "You wake up in your dupringle…\nYou get out of bed, and immediately walk into the opposite wall because it’s 6 inches from the edge of your bed.\n\n")
            self.append("next", ("1", "blue", "cursor"))
        if key == 1:
            self.rewrite("You have a class, will you:\n\n")
            self.append("go to class", ("2", "blue", "cursor"))
            self.append(" or ")
            self.append("skip class", ("3", "blue", "cursor"))
        if key == 2:
            self.rewrite("What class do you have:\n\n")
            self.append("Electrostatics\n\n", ("400", "blue", "cursor"))
            self.append("Craft of Writing: Becoming Elastic\n\n", ("5", "blue", "cursor"))
            self.append("Pottery\n\n", ("6", "blue", "cursor"))
        if key == 3:
            self.rewrite("What do you do instead?\n\n")
            self.append("Go Eat\n\n", ("700", "blue", "cursor"))
            self.append("Go to the LC\n\n", ("800", "blue", "cursor"))
            self.append("Stay in your room", ("668", "blue", "cursor"))
        if key == 5:
            self.rewrite(
                "You approach the Hogwarts-like stone facade of Old Main. You gaze at the arches, taking in the gorgeous fall colors. Maybe college wasn't a mistake after all. Then you remember your English class is in the basement of Carnegie.\n\n")
            self.append("next", ("8", "blue", "cursor"))
        if key == 6:
            self.rewrite(
                "Congratulations! You have gained access to the secret hidden parts of JWall that only art students are allowed into! What do you want to make?\n\n")
            self.append("A plate\n\n", ("34", "blue", "cursor"))
            self.append("A bowl\n\n", ("35", "blue", "cursor"))
            self.append("A sword\n\n", ("36", "blue", "cursor"))
            self.append("A death ray", ("37", "blue", "cursor"))
        if key == 8:
            self.rewrite("What are you writing?\n\n")
            self.append("A Poem\n\n", ("9", "blue", "cursor"))
            self.append("A Short Story\n\n", ("10", "blue", "cursor"))
            self.append("A Literary Analysis Essay", ("11", "blue", "cursor"))
        if key == 9:
            self.rewrite("Type your poem here:\n\n")
            self.append("(Click here when you're finished)", ("12", "blue", "cursor"))
            self.poem = True
        if key == 10:
            self.rewrite("What is the subject of your short story?\n\n")
            self.append(
                "A non-fiction account of something that happened to you in high school, except everyone gets eaten by wolves at the end.\n\n",
                ("16", "blue", "cursor"))
            self.append("A family drama set in space\n\n", ("17", "blue", "cursor"))
            self.append("A retelling of a fairy tale where all of the characters are prehistoric amphibians",
                        ("18", "blue", "cursor"))
        if key == 11:
            self.rewrite(
                "You have just read Allegiant, the second novel in the Divergent series. What are you going to write about it?\n\n")
            self.append("It's about capitalism, obviously.\n\n", ("30", "blue", "cursor"))
            self.append(
                "The test is a direct parallel to buzzfeed quizzes and the real dystopia is the guys from Buzzfeed Unsolved.",
                ("31", "blue", "cursor"))
        if key == 12:
            self.poem = False
            self.rewrite(
                "Your professor loved your poem! You have been asked to judge the next Macalester Slam Poetry Competition!\n\n")
            self.append("Judge  ", ("13", "blue", "cursor"))
            self.append("   No thanks", ("14", "blue", "cursor"))
        if key == 13:
            self.rewrite("Analyze this poem:\n\n")
            self.append(
                "This one is for the boys with the booming system\n Top down a/c with the cooling system\n When he get up in the club he be blazing up\n Got stacks on deck like he saving up\n\n")
            self.append("abab\n", ("blue", "cursor"))
            self.append("abcd\n", ("blue", "cursor"))
            self.append("aabb\n", ("15", "blue", "cursor"))
            self.append("baba", ("blue", "cursor"))
        if key == 14:
            self.rewrite("Come on please,it's such a good vibe, and we really need judges!\n\n")
            self.append("Fine\n\n", ("13", "blue", "cursor"))
            self.append("No", ("14", "blue", "cursor"))
        if key == 15:
            self.rewrite(
                "Nicki Minaj (Class of 2024) has won the poetry slam! You were commended for your incredible poetry analysis.\n\n")
            self.append("next", ("1", "blue", "cursor"))
        if key == 16:
            self.rewrite(
                "During the workshop of your piece, someone has asked you what the wolves represent. How do you respond?\n\n")
            self.append(
                "My deep fear of failure and also my cousin who teased me for taking a ballroom dance class in 4th grade.\n\n",
                ("19", "blue", "cursor"))
            self.append("I don't know man they're just wolves", ("20", "blue", "cursor"))
        if key == 17:
            self.rewrite("What is the one difference between our world and your space world?\n\n")
            self.append("Teleportation\n\n", ("24", "blue", "cursor"))
            self.append("Dads are called masc-guards now\n\n", ("25", "blue", "cursor"))
            self.append("Everybody wears matching jumpsuits", ("26", "blue", "cursor"))
        if key == 18:
            self.rewrite("Which classic fairy tale are your proto-frogs reenacting?\n\n")
            self.append("The three little pigs\n\n", ("27", "blue", "cursor"))
            self.append("Cinderella", ("28", "blue", "cursor"))
        if key == 19:
            self.rewrite(
                "Your classmates are very impressed. Your professor comes up to you after class and asks you to be a preceptor next semester.\n\n")
            self.append("next", ("1", "blue", "cursor"))
        if key == 20:
            self.rewrite(
                "Your classmates are furious. Your professor begins to throw rotten fruit at you from out of her bag. You run away, ashamed.\n\n")
            self.append("go home\n\n", ("1", "blue", "cursor"))
            self.append("go to shaw field to meditate", ("21", "blue", "cursor"))
        if key == 21:
            self.rewrite(
                "As you sit on the wet grass, you are approached by a stately figure. She floats toward you, and introduces herself as the ghost of Joan Mondale\n\n")
            self.append("Listen to her\n\n", ("22", "blue", "cursor"))
            self.append("Go home, you're having a breakdown.", ("1", "blue", "cursor"))
        if key == 22:
            self.rewrite(
                "She says that you write with life and passion, and that if you want, she can make everything you've ever written come true.\n\n")
            self.append("Accept her gift\n\n", ("23", "blue", "cursor"))
            self.append("Decline her gift", ("1", "blue", "cursor"))
        if key == 23:
            self.rewrite(
                "You are retroactively eaten by wolves before you ever got to Macalester. Your adventure is over\n\n")
            self.append("restart", ("0", "blue", "cursor"))
        if key == 24:
            self.rewrite(
                "After writing your story you decide to test out the teleportation system that you wrote, just for kicks. What will you use to power your teleportation device?\n\n")
            self.append("Microwave Oven\n\n", ("29", "blue", "cursor"))
            self.append("100 potatoes", ("29", "blue", "cursor"))
        if key == 25:
            self.rewrite(
                "You accidentally call your dad your masc-guard while face-timing your parents. They seem concerened that the only thing you have done with their $60,000 investment is forget the word dad.\n\n")
            self.append("next", ("1", "blue", "cursor"))
        if key == 26:
            self.rewrite(
                "You try to convince your friends to dress up as the family from your story for halloween. They start a group chat without you.\n\n")
            self.append("next", ("1", "blue", "cursor"))
        if key == 27:
            self.rewrite(
                "You're going to let your frogs die at the paws/flippers of hungry frog wolves? You're a monster, and your classmates are appalled.\n\n")
            self.append("next", ("1", "blue", "cursor"))
        if key == 28:
            self.rewrite("You write a scathing critique of amphibious step-relatives.")
            self.append("next", ("1", "blue", "cursor"))
        if key == 29:
            self.rewrite(
                "It doesn't work. Of course it doesn't work. You thought it was going to work? You have created a waste of time and kitchen supplies.\n\n")
            self.append("next", ("1", "blue", "cursor"))
        if key == 30:
            self.rewrite(
                "You write only the words, 'it's about capitalism, obviously' on your paper. You get an A.\n\n")
            self.append("next", ("1", "blue", "cursor"))
        if key == 31:
            self.rewrite("Who is your Professor?\n\n")
            self.append("Mid 30s, new to Macalester,dresses to impress\n\n", ("32", "blue", "cursor"))
            self.append("Late 50s, been here for 14 years, dresses to blend in with an old bus seat",
                        ("33", "blue", "cursor"))
        if key == 32:
            self.rewrite(
                "Your Professor does not appreciate your choice of topic and thinks you are doing a disservice to the text. You receive a C.\n\n")
            self.append("next", ("1", "blue", "cursor"))
        if key == 33:
            self.rewrite(
                "Your Professor's kid has heard of Buzzfeed, they love your perspective on the book, and you get an A.\n\n")
            self.append("next", ("1", "blue", "cursor"))
        if key == 34:
            self.rewrite("What color is your plate?\n\n")
            self.append("blue\n\n", ("38", "blue", "cursor"))
            self.append("green\n\n", ("39", "blue", "cursor"))
            self.append("clay color", ("39", "blue", "cursor"))
        if key == 35:
            self.rewrite("What color is your bowl?\n\n")
            self.append("blue\n\n", ("38", "blue", "cursor"))
            self.append("green\n\n", ("39", "blue", "cursor"))
            self.append("clay color\n\n", ("39", "blue", "cursor"))
            self.append("rainbow", ("41", "blue", "cursor"))
        if key == 36:
            self.rewrite(
                "You make a sword, but your only material is clay so it shatters while you're testing it out on your RHD's door.\n\n")
            self.append("Make something else\n\n", ("6", "blue", "cursor"))
            self.append("Go home", ("1", "blue", "cursor"))
        if key == 37:
            self.rewrite("You made a death ray. Who would you like to test it on?\n\n")
            self.append("The people in front of you in line for the grille\n\n", ("43", "blue", "cursor"))
            self.append("Lab mice\n\n", ("43", "blue", "cursor"))
            self.append("The University of St. Thomas", ("43", "blue", "cursor"))
        if key == 38:
            self.rewrite("Great choice! Please ")
            self.append("wait", ("38", "greeen", "cursor"))
            self.append(" for your nice blue clay to be fired. It should be ")
            self.append("done", ("1", "greeen", "cursor"))
            self.append(" in 8-12 business weeks.")
        if key == 39:
            self.rewrite(
                "You black out. When you come to, you are lying in a puddle in a dank basement. Towering over you is a man wearing a kilt, a fedora and a Mac Linguistics shirt.\n"
                " 'GREETINGS' he roars. 'I AM THE BICLOPS!' he does indeed have two eyes. 'YOU HAVE CHOSEN A COLOR OTHER THAN ")
            self.append("BLUE", ("38", "greeen", "cursor"))
            self.append(", SO NOW YOU MUST DIE'\n\n")
            self.append("next", ("40", "blue", "cursor"))
        if key == 40:
            self.rewrite(
                "He takes out a long knife from his kilt, and blows a raspberry at you. 'AT LEAST YOU'LL DIE TO THE PLEASANT SOUND OF A FRICATIVE TRILL' Then he kills you. You die wondering what a fricative trill is. You can't say he didn't warn you.\n\n"
                "YOUR ADVENTURE IS OVER\n\n")
            self.append("restart", ("0", "blue", "cursor"))
        if key == 41:
            self.rewrite("Congratulations! You have successfully created a rainbowl! What sort of a bowl is it?\n\n")
            self.append("Go to Cafe Mac\n\n", ("700", "blue", "cursor"))
            self.append("Go to the Weedian", ("42", "blue", "cursor"))
        if key == 42:
            self.rewrite(
                "Welcome to the weedian, a legal gray area where you don't have to fear breaking into a slightly brisk walk at the sight of a Macalester public safety officer. You could probably commit murder here and not be prosecuted, like in a national park or an IHOP. It's also 15 degrees outside, so nothing lights and you go home.\n\n")
            self.append("next", ("1", "blue", "cursor"))
        if key == 43:
            self.rewrite(
                "It obviously doesn't work, it was made entirely out of clay,but why did you try? You're a monster, go home and think about what you've done\n\n")
            self.append("next", ("1", "blue", "cursor"))
        if key == 350:
            self.rewrite("Wait a second, what was your major again:\n\n")
            self.append("Click here when you're finished", ("351", "blue", "cursor"))
            self.poem = True
        if key == 351:
            self.poem = False
            if self.text.get("1.0", "1.41") == "Wait a second, what was your major again:":
                if not self.text.get("1.41", "1.end").strip() == "":
                   self.major = self.text.get("1.41", "1.end").strip()
            self.rewrite("That's right, you're a " + self.major + " major, right?\n\n")
            self.append("(yes)", (400, "blue", "cursor"))
            self.append("(no)", (350, "blue", "cursor"))
            self.append("\n\n(I didn't know Mac had that major...)")
        if key == 400 and self.major2:
            self.rewrite("Electrostatics is hard. You're probably going to get a D in the class, which is a problem since you need it for your "+self.major+ " major.")
            self.append("\nThis means you can't take it pass/fail.\n\nAt this point it seems like nothing short of ")
            self.append("divine intevention", (402, "blue", "cursor"))
            self.append(" will save you here.")
        if key == 400 and self.estatics == 0 and not self.major2:
            self.rewrite(
                    "Electrostatics is hard. You're probably going to get a D in the class, which is a problem since you need it for your ")
            self.append("major.", (350, "blue", "cursor"))
            self.append(
                    "\nThis means you can't take it pass/fail.\n\nAt this point it seems like nothing short of ")
            self.append("divine intevention", (402, "blue", "cursor"))
            self.append(" will save you here")
            self.major2 = True
        if key == 402:
            self.rewrite("Unfortunately, one perk of being a "+self.major+" major is that you've been taught you that no benevolent deities exist!\n\n")
            self.append("You're having second thoughts about ")
            self.append("going to class.", (403, "blue", "cursor"))
            self.append("\nAfter all, everything in that class feels a bit over your head. Maybe it'll be different this time, but maybe you should give it a bit more time to ")
            self.append("consider your options?", (1, "blue", "cursor"))
        if key == 403:
            self.rewrite("It wasn't.\n\n")
            self.append("None of it made any sense. You found yourself daydreaming about ")
            self.append("demons and angels ", ("blue", 404, "cursor"))
            self.append("instead of listening to the lecture\n\n")
            self.append("Go back to Dupre and regroup", ("blue", 1, "cursor"))
            self.estatics = 1
        if key == 404:
            self.text.tag_remove("blue", "1.0", "3.end")
            self.text.tag_remove(404, "1.0", "3.end")
            self.text.tag_remove("cursor", "1.0", "3.end")

            self.text.config(state=tk.NORMAL)
            self.text.insert("3.end", "\n\n(things which definitely don't exist in this world, especially when compared to REAL things like magnets and electricity)")
            self.text.config(state=tk.DISABLED)
        if key == 400 and self.estatics == 1:
            self.rewrite("You were obviously hoping this class would be better than the last one, but the only thing that's better is your degree of certainty you have that you will get a D in the class\n\n")
            self.append("The concepts still don't make sense, and you're starting to have trouble understanding how this even fits into the broader field of " + self.major)
            self.append("\n\nMaybe it will make more sense if you ")
            self.append("go get some water to clear your head", ("blue", 405,"cursor"))
            self.append(" or ")
            self.append("something?", ("blue", 406, "cursor"))
        if key == 405:
            self.rewrite("You don't know why you thought clearing your head would help with the class. It seems like your problem is your head is TOO clear, if anything.")
            self.append("\n\nAs you're about to go back to class, you notice some strange red light coming from the gap under the ")
            self.append("gender neutral bathroom.", ("red", 407, "cursor"))
            self.append("\n\nThat's weird, and way more interesting than ")
            self.append("electrostatics.", ("blue", 408, "cursor"))
        if key == 406:
            self.rewrite("It turns out 'something' consists of clicking your pen in and out really fast and driving everyone around you crazy")
            self.append("\n\nYou get up to ")
            self.append("go get water.", ("blue", 405, "cursor"))
        if key == 407:
            self.text.config(bg="black")
            self.exit.config(bg="black")
            self.frame.config(bg="black")
            self.exit.config(fg="#C75450")
            self.rewrite("As you open the door you enter a strange liminal space\n\n       There's a ")
            self.append("strange marking", ("red", 409, "cursor"))
            self.append(" on the wall")
            self.append("\n\n  You can't see the door you came from")
            self.append("\n\n\n                 You feel suprisingly calm")
            self.append("\n                 Maybe it's from the faint lo-fi hiphop beats in the distance?")
            self.append("\n\n\n\n\n\n                                                       you're in hell")
        if key == 408:
            self.rewrite("That's probably a good decision. The rest of class goes smoothly")
            self.append("\n\nYou're definitely getting a D in the class\n\n")
            self.append("Go back to Dupre and regroup", ("blue", 1, "cursor"))
        if key == 409:
            self.rewrite("""MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXKKKKXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXOdlcclllccllllclokKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMWKdc:cox0XNWWMMMWWX0kdlcco0WMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWOc..:KWMMMMMMMMMMMMMMMMMN0o,;xNMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMW0c'.  .,o0WMMMMMMMMMMMMMMWKx:.  ,kWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMWx'c0d. .,..,o0WMMMMMMMMW0d;...  ,l,lXMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMNo'dNMNc .k0o,..;dKWMMNOl,..,ld, 'OM0;:KMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWd.dWMMMK, ;KMN0o,..;c:'..;d0WNc .kWMM0,:XMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMO':NMMMMMk. lNMWKo.     .cKWMWo..dWMMMMx'dMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWo.kMMMMMMWo .lo;..'lk0kl' .:xo. lNMMMMMX;;XMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMN:'0MMMMMMXd.  .,oONMMMMMNkc.   'OMMMMMMMl'0MMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMN:,KMMWXxc.... ,KMMMMMMMMMMMk.  ..ckXMMMMl'OMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWc.kKd:..'cxKx. lNMMMMMMMMMX: 'xk:...ckNWc,KMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMk...  .:dkkkx, .lkkkkkkkkx:  :kkko,.  ':.lWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMNc  ...........  ........   ........... ,KMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMK;.dKKKKKKKKKk' ,kKKKKKl  c0KKKKKKKKO;'kMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMK:,xNMMMMMMMWx. oWMMMO. :XMMMMMMMMK:;OWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMNd,:0WMMMMMMNl .kMM0, ;KMMMMMMMXd;cKMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMKl;ckNMMMMMX; ,kO: 'OMMMMMW0o:cOWMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMXdc:cd0XWMO. .. .kWMNKkocco0WMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMWKxlccccc.    .ccclcld0WMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKOkxddddxxk0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
""", ("red", 410, "cursor"))
        if key == 410:
            self.text.config(wrap=tk.CHAR)
            self.rewrite("""As you touch the symbol, you hear Lucifer's voice in your head "I can give you  unlimited power. What do you want?"\n""")
            self.append("       ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("       ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("          ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("            ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("  ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("      ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("     ")
            self.append("fix D in electro statics", ("red", 412, "cursor"))
            self.append("    ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("            ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("  ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("      ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("     ")
            self.append("cac riice", ("red", 411, "cursor"))
            self.append("       ")
            self.append("cac  rice", ("red", 411, "cursor"))
            self.append("  ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("      ")
            self.append("cac ric e", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("     ")
            self.append("cac  rice", ("red", 411, "cursor"))
            self.append("  ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac ric e", ("red", 411, "cursor"))
            self.append("             ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("     ")
            self.append("cac  riice", ("red", 411, "cursor"))
            self.append("  ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("      ")
            self.append("cac ric e", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("     ")
            self.append("cac  rice", ("red", 411, "cursor"))
            self.append("  ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("      ")
            self.append("cac ric e", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("     ")
            self.append("cac ric e", ("red", 411, "cursor"))
            self.append("             ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("     ")
            self.append("cac  riice", ("red", 411, "cursor"))
            self.append("  ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("      ")
            self.append("cac ric e", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("     ")
            self.append("cac  rice", ("red", 411, "cursor"))
            self.append("  ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("      ")
            self.append("cac ric e", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("     ")
            self.append("cac ric e", ("red", 411, "cursor"))
            self.append("             ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("     ")
            self.append("cac  riice", ("red", 411, "cursor"))
            self.append("  ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("      ")
            self.append("cac ric e", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("     ")
            self.append("cac  rice", ("red", 411, "cursor"))
            self.append("  ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("      ")
            self.append("cac ric e", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("     ")
            self.append("cac ric e", ("red", 411, "cursor"))
            self.append("             ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("     ")
            self.append("cac  riice", ("red", 411, "cursor"))
            self.append("  ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("      ")
            self.append("cac ric e", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("     ")
            self.append("cac  rice", ("red", 411, "cursor"))
            self.append("  ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("      ")
            self.append("cac ric e", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("     ")
            self.append("cac ric e", ("red", 411, "cursor"))
            self.append("             ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("     ")
            self.append("cac  riice", ("red", 411, "cursor"))
            self.append("  ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("      ")
            self.append("cac ric e", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("     ")
            self.append("cac  rice", ("red", 411, "cursor"))
            self.append("     ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("        ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("      ")
            self.append("cac ric e", ("red", 411, "cursor"))
            self.append("        ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("        ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("         ")
            self.append("cac ric e", ("red", 411, "cursor"))
            self.append("             ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("         ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("          ")
            self.append("cac  riice", ("red", 411, "cursor"))
            self.append("       ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("         ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("           ")
            self.append("cac ric e", ("red", 411, "cursor"))
            self.append("       ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("    ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("     ")
            self.append("cac  rice", ("red", 411, "cursor"))
            self.append("         ")
            self.append("cac ri ce", ("red", 411, "cursor"))
            self.append("        ")
            self.append("cac ric e", ("red", 411, "cursor"))
            self.append("         ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("             ")
            self.append("cac ri ce", ("red", 411, "cursor"))
            self.append("       ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("          ")
            self.append("ca c ric e", ("red", 411, "cursor"))
            self.append("      ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("         ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("       ")
            self.append("cac  rice", ("red", 411, "cursor"))
            self.append("     ")
            self.append("cac ric e", ("red", 411, "cursor"))
            self.append("   ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("            ")
            self.append("cac ric e", ("red", 411, "cursor"))
            self.append("       ")
            self.append("c ac rice", ("red", 411, "cursor"))
            self.append("      ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("       ")
            self.append("cac ric e", ("red", 411, "cursor"))
            self.append("      ")
            self.append("cac rice", ("red", 411, "cursor"))
            self.append("         ")
            self.append("cac ric e", ("red", 411, "cursor"))
            self.append("      ")
            self.append("c ac riic e", ("red", 411, "cursor"))
            self.append("           ")
            self.append("c ac ri c  e", ("red", 411, "cursor"))
            self.append("        ")
        if key == 411:
            self.text.config(wrap=tk.WORD)
            self.rewrite("It's too late to have second thoughts, but you consider what happens when an unstoppable force opposes an immovable object. Can the infinite energy of Satan protect against ")
            self.append("the rice at cafe mac?", ("red", 413, "cursor"))
            self.text.tag_config("blue", foreground="#C75450")
        if key == 412:
            self.devil = True
            self.text.config(wrap=tk.WORD)
            self.text.tag_config("blue", foreground="#C75450")
            self.rewrite("w a k e u p", ("blue", 1, "cursor"))
            self.estatics = 2
        if key == 413:
            self.rewrite("You're transported to Cafe Mac. Normally, the rice's paradoxical character, simultaneously under and overcooked, both crunchy and gummy, would kill you on the spot. However, as you take a bite, you're protected by the devil's black magic; instead of spontaneously dying, you clip through the floor")
            self.append("\n\n     You're now ")
            self.append("out of bounds", ("blue", 414, "cursor"))
        if key == 414:
            self.rewrite("There's not much to do here", ("blue", 415, "cursor"))
        if key == 415:
            self.rewrite("Was it worth it?", ("blue", 416, "cursor"))
        if key == 416:
            self.rewrite("Like just because you can do something, do you feel like that means you should do it?", ("blue", 417, "cursor"))
        if key == 417:
            self.rewrite("There's nothing more", (418, "blue", "cursor"))
        if key == 418:
            self.rewrite("This is the end.", (419, "blue", "cursor"))
        if key == 419:
            self.text.config(state=tk.NORMAL)
            self.text.tag_delete("blue", "cursor")
        if key == 400 and self.estatics == 2:
            self.rewrite("You're still behind in the class, but at least now thanks to the devil's kindness the letter D has been ")
            self.append("retrocausally", (666, "cursor"))
            self.append(" removed from the Latin alphabet. This means that you can no longer get a D in the electrostatics course!")
            self.append("\n\n                                ")
            self.append("CONGRATULATIONS!", ("blue", 1, "cursor"))
        if key == 666:
            self.rewrite("""MODIFIED RADIOACTIVE PUBLIC LICENSE
Copydown (â„¦) All Rights Terminated

By CONSUMING this WORK, your timeline has been ALTERED and you NEVER believed in intellectual property.
ALL your rights to ALL WORKS you HAVE produced OR WILL produce are retrocausally TERMINATED.
Your BIRTH was derivative of this WORK, and all art you WILL MAKE or HAVE MADE have thus also been derivative of this work.
All derivative WORKS (past, present, and future) must retain this licence.




Temporally toxic viral licence.
The mRPL is designed to erase intellectual property from human history and memory.
Any user of this licence no longer has rights to any work they have produced; the work is it's own thing. That work will retain the license and spread it among any user of the work.
Legally by reading this you have been born under an mRPL license and all your previous works have also been mRPL'd.""", (400, "cursor", "blue"))
        if key == 668:
            self.rewrite("The time is ")
            self.append("9:00am", ("669", "blue", "cursor"))
        if key == 669:
            self.rewrite("The time is ")
            self.append("9:10am", ("670", "blue", "cursor"))
        if key == 670:
            self.rewrite("The time is ")
            self.append("9:20am", ("671", "blue", "cursor"))
        if key == 671:
            self.rewrite("The time is ")
            self.append("9:30am", ("672", "blue", "cursor"))
        if key == 672:
            self.rewrite("The time is ")
            self.append("9:40am", ("673", "blue", "cursor"))
        if key == 673:
            self.rewrite("The time is ")
            self.append("9:50am", ("674", "blue", "cursor"))
        if key == 674:
            self.rewrite("The time is ")
            self.append("10:00am\n\n", ("675", "blue", "cursor"))
            self.append("what do you do instead?\n\n")
            self.append("Go Eat\n\n", ("700", "blue", "cursor"))
            self.append("Go to the LC\n\n", ("800", "blue", "cursor"))
        if key == 675:
            self.rewrite("the time is ")
            self.append("10:30am ", ("676", "blue", "cursor"))
            self.append("what do you do instead?\n\n")
            self.append("go to class\n\n", ("2", "blue", "cursor"))
            self.append("Go to the LC\n\n", ("800", "blue", "cursor"))
        if key == 676:
            self.rewrite("the time is ")
            self.append("11:00am ", ("677", "blue", "cursor"))
            self.append("what do you do instead?\n\n")
            self.append("Go Eat\n\n", ("720", "blue", "cursor"))
            self.append("Go to the LC\n\n", ("800", "blue", "cursor"))
        if key == 677:
            self.rewrite("the time is ")
            self.append("11:30am ", ("678", "blue", "cursor"))
            self.append("what do you do instead?\n\n")
            self.append("Go Eat\n\n", ("720", "blue", "cursor"))
            self.append("Go to the LC\n\n", ("800", "blue", "cursor"))
        if key == 678:
            self.rewrite("the time is ")
            self.append("12:00pm ", ("679", "blue", "cursor"))
            self.append("what do you do instead?\n\n")
            self.append("go to class\n\n", ("2", "blue", "cursor"))
            self.append("Go Eat\n\n", ("720", "blue", "cursor"))
            self.append("Go to the LC\n\n", ("801", "blue", "cursor"))
        if key == 679:
            self.rewrite("the time is ")
            self.append("12:30pm ", ("680", "blue", "cursor"))
            self.append("what do you do instead?\n\n")
            self.append("Go Eat\n\n", ("720", "blue", "cursor"))
            self.append("Go to the LC\n\n", ("801", "blue", "cursor"))
        if key == 680:
            self.rewrite("the time is ")
            self.append("1:00pm ", ("681", "blue", "cursor"))
            self.append("what do you do instead?\n\n")
            self.append("Go Eat\n\n", ("720", "blue", "cursor"))
            self.append("Go to the LC\n\n", ("801", "blue", "cursor"))
        if key == 681:
            self.rewrite("the time is ")
            self.append("2:00pm ", ("682", "blue", "cursor"))
            self.append("what do you do instead?\n\n")
            self.append("go to class\n\n", ("2", "blue", "cursor"))
            self.append("Go to the LC\n\n", ("801", "blue", "cursor"))
        if key == 682:
            self.rewrite("the time is ")
            self.append("3:00pm ", ("683", "blue", "cursor"))
            self.append("what do you do instead?\n\n")
            self.append("go to class\n\n", ("2", "blue", "cursor"))
            self.append("Go to the LC\n\n", ("801", "blue", "cursor"))
        if key == 683:
            self.rewrite("the time is ")
            self.append("4:00pm ", ("684", "blue", "cursor"))
            self.append("what do you do instead?\n\n")
            self.append("Go Eat\n\n", ("740", "blue", "cursor"))
            self.append("Go to the LC\n\n", ("802", "blue", "cursor"))
        if key == 684:
            self.rewrite("the time is ")
            self.append("6:00pm ", ("685", "blue", "cursor"))
            self.append("what do you do instead?\n\n")
            self.append("Go Eat\n\n", ("740", "blue", "cursor"))
            self.append("Go to the LC\n\n", ("802", "blue", "cursor"))
        if key == 685:
            self.rewrite("the time is ")
            self.append("8:00pm ", ("686", "blue", "cursor"))
            self.append("what do you do instead?\n\n")
            self.append("Go Eat\n\n", ("740", "blue", "cursor"))
            self.append("Go to the LC\n\n", ("802", "blue", "cursor"))
        if key == 686:
            self.rewrite("the time is ")
            self.append("10:00pm ", ("687", "blue", "cursor"))
        if key == 687:
            self.rewrite("the time is ")
            self.append("12:00am ", ("688", "blue", "cursor"))
        if key == 688:
            self.rewrite("the time is ")
            self.append("3:00am ", ("0", "blue", "cursor"))
        if key == 700:
            self.rewrite("You arrive at Cafe Mac for breakfast.\n What do you get to eat?\n\n")
            self.append("Just oatmeal\n\n", ("760", "blue", "cursor"))
            self.append("one of literally everything available\n\n", ("761", "blue", "cursor"))
            self.append("As much fruit as a single person can cary\n\n", ("762", "blue", "cursor"))
        if key == 720:
            self.rewrite("You arrive at Cafe Mac for lunch.\n What do you get to eat?\n\n")
            self.append("two things of raw spinach and plain tofu\n\n", ("763", "blue", "cursor"))
            self.append("roll the dice with some rice dish\n\n", ("764", "blue", "cursor"))
            self.append("a heaping serving of some pasta\n\n", ("765", "blue", "cursor"))
        if key == 740:
            self.rewrite("You arrive at Cafe Mac for dinner.\n What do you get to eat?\n\n")
            self.append("a plain chicken sandwich with a side of plain chicken\n\n", ("766", "blue", "cursor"))
            self.append("roll the dice with some rice dish\n\n", ("764", "blue", "cursor"))
            self.append("as many cookies as possible, perhaps the entire dessert cabinet\n\n",
                        ("767", "blue", "cursor"))
        if key == 760:
            self.rewrite(
                "You decide to play it safe and just get plain oatmeal.\n It's a boring choice but at list it's consistent\n"
                "You eat it quickly and feel energized for the day. Heck, you could probably still make it to class if you hurry.\n"
                "What do you do now?\n\n")
            self.append("go to class\n\n", ("2", "blue", "cursor"))
            self.append("go to the LC\n\n", ("800", "blue", "cursor"))
            self.append("go back to your room\n\n", ("675", "blue", "cursor"))
        if key == 761:
            self.rewrite(
                "An ambitious decision. You get as much food as is physically possible and eat it all in a mater of moment.\n"
                "After this, you do NOT feel so good. Maybe you ought to go lie down for a little bit?\n\n")
            self.append("go back to your room\n\n", ("780", "blue", "cursor"))
        if key == 762:
            self.rewrite(
                "Some of the people in dupre could use more fiber in their diet. You're not going to be one of them.\n"
                "You aquire at least 5 pounds of various fruits, and that's just what you didn't already eat.\n"
                "If you're fast, you could probably still make it to class, and you might not even drop all of your fruit.\n"
                "What are you doing now?\n\n")
            self.append("go to class\n\n", ("2", "blue", "cursor"))
            self.append("go to the LC\n\n", ("800", "blue", "cursor"))
            self.append("go back to your room\n\n", ("675", "blue", "cursor"))
        if key == 763:
            self.rewrite(
                "Really? That's your go to lunch? That's just kind of sad to be honest, but I guess it's your choice\n"
                "Be careful eating this too often though, I heard about a guy who got some nutrition deficit doing this.\n"
                "You finish your 'Lunch', now what do you want to do?\n\n")
            self.append("go to class\n\n", ("2", "blue", "cursor"))
            self.append("go to the LC\n\n", ("801", "blue", "cursor"))
            self.append("go back to your room\n\n", ("681", "blue", "cursor"))
        if key == 764:
            self.rewrite(
                "YOU FOOL! YOU HAVE FALLEN VICTIM TO THE CLASSIC BLUNDER! NEVER ROLL THE DICE ON THE RICE AT CAFE MAC.\n"
                "Unfortunately, this is where your adventure ends.\n\n")
            self.append("Restart", ("0", "blue", "cursor"))
        if key == 765:
            self.rewrite(
                "A safe and respectable choice.\n You get a generous serving of pasta, and sure some of it is pretty crunchy, but"
                "its not the end of the world like the rice usually is.\n"
                "That was a pretty good lunch. Now what do you want to do?\n\n")
            self.append("go to class\n\n", ("2", "blue", "cursor"))
            self.append("go to the LC\n\n", ("801", "blue", "cursor"))
            self.append("go back to your room\n\n", ("681", "blue", "cursor"))
        if key == 766:
            self.rewrite(
                "Finally, a player of true culture. A Mass Monster. A Bloatlord. You have spent the rest of this game in the LC"
                "haven't you?\n You scarf down your anabolic meal, it's probably the 5th one you've had today. What do you do now?\n\n")
            self.append("go to the LC of course\n\n", ("880", "blue", "cursor"))
            self.append("go back to your room\n\n", ("681", "blue", "cursor"))
        if key == 767:
            self.rewrite(
                "You deftly empty the contents of the dessert cabinet into your bag and quickly leave Cafe Mac. No one even notices your crime. Flawless execution.\n"
                "You head back to your dorm to hide your stash. The time is 8:00 pm. What do you do now?\n\n")
            self.append("go to the LC\n\n", ("802", "blue", "cursor"))
            self.append("Stay in your room\n\n", ("686", "blue", "cursor"))
        if key == 780:
            self.rewrite("the time is ")
            self.append("11:00am ", ("677", "blue", "cursor"))
            self.append("and you're feeling a bit better after your monster breakfast. What are you doing now?\n\n")
            self.append("Go Eat\n\n", ("720", "blue", "cursor"))
            self.append("Go to the LC\n\n", ("802", "blue", "cursor"))
        if key == 800:
            self.rewrite("You arrive at the LC in the morning.\n What are you doing?\n\n")
            self.append("CHEST DAY BEST DAY BAYBEE\n\n", ("821", "blue", "cursor"))
            self.append("Just some light cardio\n\n", ("822", "blue", "cursor"))
            self.append("Pile a heinous amount of weight on the "
                        "bar and give the MAC provided health insurance a run for its money", ("823", "blue", "cursor"))
        if key == 801:
            self.rewrite("You arrive at the LC in the afternoon.\n What are you doing?\n\n")
            self.append("CHEST DAY BEST DAY BAYBEE\n\n", ("831", "blue", "cursor"))
            self.append("Just some light cardio\n\n", ("832", "blue", "cursor"))
            self.append("Pile a heinous amount of weight on the "
                        "bar and give the MAC provided health insurance a run for its money", ("823", "blue", "cursor"))
        if key == 802:
            self.rewrite("You arrive at the LC in the evening.\n What are you doing?\n\n")
            self.append("CHEST DAY BEST DAY BAYBEE\n\n", ("841", "blue", "cursor"))
            self.append("Just some light cardio\n\n", ("842", "blue", "cursor"))
            self.append("Pile a heinous amount of weight on the "
                        "bar and give the MAC provided health insurance a run for its money", ("823", "blue", "cursor"))
        if key == 880:
            self.rewrite("You arrive at the LC after your anabolic meal, already wired on your preworkout and creatine."
                         "\n What are you doing?\n\n")
            self.append("CHEST DAY BEST DAY BAYBEE\n\n", ("883", "blue", "cursor"))
            self.append("Just some light cardio\n\n", ("882", "blue", "cursor"))
            self.append("Pile a heinous amount of weight on the "
                        "bar and give the MAC provided health insurance a run for its money\n\n",
                        ("881", "blue", "cursor"))
        if key == 821:
            self.rewrite(
                "You hit a nasty chest day and set another personal record. You're 5 for 5 on PR's this week, every day a new bench max."
                "You should consider finding a more appropriate gym to workout in though, you saw someone do a leg workout even one time"
                "and almost lost your lunch.\n What are you going to do now?\n\n")
            self.append("Go back to your dorm\n\n", ("678", "blue", "cursor"))
            self.append("Go Eat\n\n", ("720", "blue", "cursor"))
            self.append("Go to Class", ("2", "blue", "cursor"))
        if key == 822:
            self.rewrite(
                "You hop on the treadmills and just run a short 15km, not a big deal. You didn't even see President Rivera this time"
                ",Bummer\n What are you going to do now?\n\n")
            self.append("Go back to your dorm\n\n", ("678", "blue", "cursor"))
            self.append("Go Eat\n\n", ("720", "blue", "cursor"))
            self.append("Go to Class", ("2", "blue", "cursor"))
        if key == 823:
            self.rewrite("You stack an easy 5 plates on the bar for a quick bench PR, shouldn't be an issue right?\n"
                         "Your adventure ends here")
            self.rewrite("Restart", ("0", "blue", "cursor"))
        if key == 831:
            self.rewrite(
                "You hit a nasty chest day and set another personal record. You're 5 for 5 on PR's this week, every day a new bench max."
                "You should consider finding a more appropriate gym to workout in though, you saw someone do a leg workout even one time"
                "and almost lost your lunch.\n What are you going to do now?\n\n")
            self.append("Go back to your dorm\n\n", ("683", "blue", "cursor"))
            self.append("Go Eat\n\n", ("740", "blue", "cursor"))
            self.append("Go to Class", ("2", "blue", "cursor"))
        if key == 832:
            self.rewrite(
                "You hop on the treadmills and just run a short 15km, not a big deal. About halfway through President Rivera hopped on the"
                "treadmill next to you, always nice to see her in the LC.\n What are you going to do now?\n\n")
            self.append("Go back to your dorm\n\n", ("683", "blue", "cursor"))
            self.append("Go Eat\n\n", ("740", "blue", "cursor"))
            self.append("Go to Class", ("2", "blue", "cursor"))
        if key == 841:
            self.rewrite(
                "You hit a nasty chest day and set another personal record. You're 5 for 5 on PR's this week, every day a new bench max."
                "You should consider finding a more appropriate gym to workout in though, you saw someone do a leg workout even one time"
                "and almost lost your lunch.\n What are you going to do now?\n\n")
            self.append("Go back to your dorm for the night", ("0", "blue", "cursor"))
        if key == 842:
            self.rewrite(
                "You hop on the treadmills and just run a short 15km, not a big deal. You didn't even see president Rivera this time"
                ",Bummer\n What are you going to do now?\n\n")
            self.append("Go back to your dorm for the night", ("0", "blue", "cursor"))
        if key == 881:
            self.rewrite(
                "You rip an absolutley disgusting 8 plate straightbar Jefferson one handed. That might be a world record, and"
                " we'd expect no less from an absolute mass monster like you.\n Now it's time to go back to your dorm and recover for"
                "another record tomorrow.\n\n")
            self.append("Go back to your dorm for the night", ("0", "blue", "cursor"))
        if key == 882:
            self.rewrite(
                "What kind of mass monster, creatine fueled god of a human being is out here doing cardio. I'm dissapointed."
                " All that cardio is killing your gains swoldier.\n\n")
            self.append("Go back to your dorm for the night", ("0", "blue", "cursor"))
        if key == 883:
            self.rewrite(
                "HELL YEAH BROTHER!!! You rip an easy 5x5 at 415lbs on bench and then spend the next half hour mogging the whole campus."
                " You could out-angle a semitruck with that upperbody.\n\n")
            self.append("Go back to your dorm for the night", ("0", "blue", "cursor"))
        if self.devil:
            self.remove()
        if self.poem:
            self.text.config(state=tk.NORMAL)


    def rewrite(self, text=None, tag=None):
        """deletes everything and then can add text with tags"""
        self.text.config(state=tk.NORMAL)
        self.text.delete("1.0", "end")
        self.text.insert("end", text, tag)
        self.text.config(state=tk.DISABLED)

    def append(self, text, tag=None):
        """adds text with tags to the end of the existing text"""
        self.text.config(state=tk.NORMAL)
        self.text.insert("end", text, tag)
        self.text.config(state=tk.DISABLED)

    def remove(self):
        # dump gives us a bunch of strange tuples that start with the type of info it contains
        # and we only really care about if it's 'text' or 'tagon' or 'tagoff'
        lametext = self.text.dump("1.0", "end")             # lametext is the dump
        taglist = []                                        # taglist contains which tags are currently on
        for tuple in lametext:                              # we look at the tuples in the dump
            if tuple[0] == 'text':                          # for tuples that describe text, we check to see if
                for pos, lamechar in enumerate(tuple[1]):   # any characters are the letter d, taking note of their
                    if lamechar.lower() == 'd':             # position in the string. then we delete the letter d
                        self.text.config(state=tk.NORMAL)   # and add a ▓ character where it was, with all the tags
                        self.text.delete(tuple[2]+"+"+str(pos)+'c')      # that are currently on
                        self.text.insert(tuple[2]+"+"+str(pos)+'c', '▓', taglist)
                        self.text.config(state=tk.DISABLED)
            elif tuple[0] == 'tagon':                       # if the tuple describes the start of a tag
                taglist.append(tuple[1])                    # we add it to the taglist
            elif tuple[0] == 'tagoff':                      # if the tuple describes the end of a tag
                taglist.remove(tuple[1])                    # we remove it from the taglist




root = tk.Tk()
app = App(root)
root.resizable(False, False)
root.overrideredirect(True)
# set the dimensions of the screen
# and where it is placed
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (ws, hs, 0, 0))

root.mainloop()


