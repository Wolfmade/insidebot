###########################################################
##             USER-CONFIGURATION SECTION                ##
###########################################################

BUILD_SPEED = .15  ## This is the time between actions.
                  ## increase this number to make the bot go slower, decrease it
                  ## to make it go faster.

CMD_PREFIX  = "." ## Change this to change what triggers the bot responds to
                  ## A one letter thing works best.
                  ## Good prefixes: !@#$%*()_+-=.,?|><
                  ## Bad prefixes: /\&~` ' "


SILENT_MODE = 0     ## If 1, the bot will only send error messages
                    ## ie: failed copy/paste/backup/restore
                    ## if 0, the bot will send all messages


ABSOLUTE_SILENT_MODE = 0 ## if 1, the bot will produce no messages whatsoever.

valid_blocks = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65 ]
block_names  = {              "air":0,"blank":0,"nothing":0,"stone":1,"grass":2,"dirt":3,"cobblestone":4,
                              "wood":5,"planks":5,"plant":6,"sapling":6,"admincrete":7,"opstone":7,"bedrock":7,
							  "water":8,"stillwater":9,"lava":10,"stilllava":11,"sand":12,"gravel":13,"goldore":14,
							  "gold ore":14,"gold":14,"ironore":15,"iron ore":15,"iron":15,"coal":16,"log":17,
							  "trunk":17,"leaves":18,"leaf":18,"sponge":19,"glass":20,"red":21,"orange":22,
							  "yellow":23,"lime":24,"green":25,"teal":26,"aqua":27,"cyan":28,"blue":29,"indigo":30,
							  "violet":31,"magenta":32,"pink":33,"black":34,"gray":35,"white":36,"yellowflower":37,
							  "yellow flower":37,"redflower":38,"red flower":38,"brownmushroom":39,
							  "brown mushroom":39,"redmushroom":40,"red mushroom":40,"goldblock":41,"ironblock":42,
							  "doublestair":43,"double stair":43,"stair":44,"brick":45,"tnt":46,"dynamite":46,
							  "books":47,"bookcase":47,"mossyrocks":48,"mossy rocks":48,"mossystone":48,"mossy stone":48,
							  "obsidian":49,"cobblestoneslab":50,"cobblestone slab":50,"stoneslab":50,"stone slab":50,
							  "rope":51,"sandstone":52,"snow":53,"fire":54,"lightpink":55,"light pink":55,"forestgreen":56,
							  "forest green":56,"brown":57,"deepblue":58,"deep blue":58,"turqoise":59,"ice":60,
							  "ceramictile":61,"ceramic tile":61,"magma":62,"pillar":63,"crate":64,"stonebrick":65,
							  "stone brick":65
                }

###########################################################
##        USER-CONFIGURATION SECTION ENDS HERE           ##
##   If you don't know what you're doing, don't change   ##
##   anything below this line. If you do, you are 100%   ##
##     on your own (unless it's a genuine programming    ##
##                      question).                       ##
###########################################################