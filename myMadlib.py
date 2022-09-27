storyFormat = '''                                        6

The other night, I woke up to a rustling in the trees. I looked outside my window to see a beam of {color} light.
Suddenly, a minature {animal} with {number} eyes floated down the beam. Half asleep and terribly confused, I approach my window. The {animal} motions with its {bodypart} for me to come closer.
In a warbling, high-pitched voice the {animal} stares me in the eyes and utters, "{conspiracytheory}." 
I blink. Just as suddenly as it appeared, it disappears in a blinding flash. I pinch myself. I make sure I can read my clock. I am not dreaming.
My head hurts.
                                                        
The End                                                 
'''                                                     
                                                        
def tellStory():                                        
    userPicks = dict()                                  
    addPick('color', userPicks)                        
    addPick('animal', userPicks)                          
    addPick('number', userPicks)
    addPick('bodypart', userPicks)
    addPick('conspiracytheory', userPicks) 
    story = storyFormat.format(**userPicks)             
    print(story)                                        
                                                        
def addPick(cue, dictionary):                           
    '''Prompt for a user response using the cue string, 
    and place the cue-response pair in the dictionary.  
    '''                                                 
    prompt = 'Enter an example for ' + cue + ': '       
    response = input(prompt)                            
    dictionary[cue] = response                          
                                                        
tellStory()                                             
input('Press Enter to end the program.')               
