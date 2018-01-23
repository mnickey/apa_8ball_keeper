from db import db
from seasons import seasons
from players import tandp
import os.path
import json
from datetime import datetime

def scorecard_banner():
        print("------------------------")
        print("__APA 8 Ball Scorecard__")
        print("------------------------")

def scorecard_positions():
    print("Which player is 'on top'/breaking?")
    top = input("Top Player: ")
    print("Which player is 'on bottom'/second to shoot?")
    bottom = input("Bottom Player: ")

def scorecard_form():
    return '''
<style>
    body {background-color: lightgray}
	table {border:5px solid black;}
    th {border: 2px solid blue;
        font-size: 16px;
        font-family: Monospace
        }
	td { border: 2px solid red;
    	font-size: 16px;
        font-family: Monospace
        }
</style>
<html>
<body>
<title>APA 8Ball Scorecard</title>
<table style="width: 50%">
    <tr>
        <th>+top+</th>
        <td style="text-align:center;">VS</td>
        <th>+bottom+</th>
<table style="width:100%">
    <tr>
        <th>Game 1</th>
            <tr><td><form action="/submit-innings">
  			<input type="text" placeholder="Innings Played"><button type="submit">Innings Played</button>
			</form><label><input type="checkbox" name="Top"> +top+</label><label><input type="checkbox" name="Bottom"> +bottom+</label></td></tr>
        <th>Game 2</th>
            <tr><td><form action="/submit-innings">
  			<input type="text" placeholder="Innings Played"><button type="submit">Innings Played</button>
			</form><label><input type="checkbox" name="Top"> +top+</label><label><input type="checkbox" name="Bottom"> +bottom+</label></td></tr>
        <th>Game 3</th>
            <tr><td><form action="/submit-innings">
  			<input type="text" placeholder="Innings Played"><button type="submit">Innings Played</button>
			</form><label><input type="checkbox" name="Top"> +top+</label><label><input type="checkbox" name="Bottom"> +bottom+</label></td></tr>
        <th>Game 4</th>
            <tr><td><form action="/submit-innings">
  			<input type="text" placeholder="Innings Played"><button type="submit">Innings Played</button>
			</form><label><input type="checkbox" name="Top"> +top+</label><label><input type="checkbox" name="Bottom"> +bottom+</label></td></tr>
        <th>Game 5</th>
            <tr><td><form action="/submit-innings">
  			<input type="text" placeholder="Innings Played"><button type="submit">Innings Played</button>
			</form><label><input type="checkbox" name="Top"> +top+</label><label><input type="checkbox" name="Bottom"> +bottom+</label></td></tr>
        <th>Gmae 6</th>
            <tr><td><form action="/submit-innings">
  			<input type="text" placeholder="Innings Played"><button type="submit">Innings Played</button>
			</form><label><input type="checkbox" name="Top"> +top+</label><label><input type="checkbox" name="Bottom"> +bottom+</label></td></tr>
        <th>Game 7</th>
            <tr><td><form action="/submit-innings">
  			<input type="text" placeholder="Innings Played"><button type="submit">Innings Played</button>
			</form><label><input type="checkbox" name="Top"> +top+</label><label><input type="checkbox" name="Bottom"> +bottom+</label></td></tr>
        <th>Game 8</th>
            <tr><td><form action="/submit-innings">
  			<input type="text" placeholder="Innings Played"><button type="submit">Innings Played</button>
			</form><label><input type="checkbox" name="Top"> +top+</label><label><input type="checkbox" name="Bottom"> +bottom+</label></td></tr>
        <th>Game 9</th>
            <tr><td><form action="/submit-innings">
  			<input type="text" placeholder="Innings Played"><button type="submit">Innings Played</button>
			</form><label><input type="checkbox" name="Top"> +top+</label><label><input type="checkbox" name="Bottom"> +bottom+</label></td></tr>
        <th>Game 10</th>
            <tr><td><form action="/submit-innings">
  			<input type="text" placeholder="Innings Played"><button type="submit">Innings Played</button>
			</form><label><input type="checkbox" name="Top"> +top+</label><label><input type="checkbox" name="Bottom"> +bottom+</label></td></tr>
    </tr>
</table>
<table style="width:25%">
    <tr>
        <th>Total Innings</th>
        	<tr><td><form action="/submit-innings">
  			<input type="text" placeholder="Innings Played"><button type="submit">Innings Played</button>
			</form></td></tr>
        <th>Defensive Shots</th>
                	<tr><td><form action="/submit-innings">
  			<input type="text" placeholder="Defensive Shots"><button type="submit">Defensive Shots</button>
			</form></td></tr>
    </tr>
</table>
</body>
</html>
'''
