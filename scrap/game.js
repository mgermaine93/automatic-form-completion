// https://project.wnyc.org/party-name-generator/#
// this can be used to generate the group name
// https://stackoverflow.com/questions/9828876/find-javascript-function-definition-in-chrome

var words;
var number_of_versions = 6;

function getWords() {
	
	// Originally planned to nab from a google spreadsheet.
	// Hardcoded for now.
	// need only do once.
	
	var data;
	
        data =
        {"political_stance": ["Liberal", "Conservative", "Independent", "Communist", "Federalist", "Socialist", "Anarchist", "Libertarian", "Democratic", "Moderate", "Centrist", "Marxist"], "single_phrase": ["Like it's 1999", "All Tomorrow's", "Pity", "Thank You Based God", "Surprise", "LAN", "Costume", "Slumber", "Stop & Frisk", "Bring Back Arrested Development", "Free Gucci", "Tread on Me", "Iced Tea", "Pizza", "After", "Paid Vacation"], "tax_person": ["the Rich", "the Poor", "Everybody", "Grandma", "Our Children", "the Future", "Nobody", "America's Job Creators", "the Huddled Masses", "Freedom", "the Dead"], "political_people": ["Liberal", "Conservative", "Independent", "Communist", "Federalist", "Socialist", "Anarchist", "Libertarian", "Democratic", "Moderate", "Centrist", "Revolutionary", "Marxist", "Bolshevik", "Single Moms", "Orphans", "Children", "Seniors", "Grandmas", "Nudist"], "political_stance_noun": ["Goon", "Agitator", "Loafer", "Thug", "Riff-Raff", "Freeloader", "Crusader", "Convict", "Martyr", "Jerk", "Blowhard", "Saint", "Backlash", "Rage", "Venom", "Revolution", "Firestorm"], "adjectives": ["New", "Athletic", "Superior", "Lazy", "Indulgent", "Angry", "Crazed", "Apathetic", "Jaded", "Salivating", "Rambunctious", "Bleeding Heart", "Manipulative", "Caffeinated", "Overhyped", "Incompetent", "Inconsiderate", "Evil", "Valiant", "Stoic", "Working", "Modern", "Old-Fashioned"], "put_nouns": ["Our Children", "Wildlife", "the Environment", "Freedom", "Sanity", "Compassion", "Pizza", "Transportation", "the Economy", "Total War", "Equal Rights", "Seniors", "Waste Management", "the Proletariat", "Currency Manipulation", "Tradition", "Families", "Justice", "the Rich", "the Poor", "World Domination", "Labor"], "general_nouns": ["Wildlife", "Alcohol", "Marijuana", "Fun", "Taxes", "Prohibition", "Pizza", "Cash", "Gold", "Freedom", "Poverty", "Values", "Chaos", "Platinum", "Equality", "Exceptionalism", "Jingoism", "Lunch Breaks"], "beginning": ["Modern", "Anti-", "Pro-", "New", "Never-Ending", "Forever", "No", "National", "American", "United", "Classic", "Traditional", "Organized", "Grassroots", "Patriots for", "Americans for", "Old-Fashioned"], "order": ["First", "Last", "Somewhere in the Middle of Our Priorities", "Off Until Tomorrow"]}
	return data;
	
}

function pickWord(kind) {
	
	// picks one of the words from the array of kinds (ie "adjective")
	// available
	
	var word;
	var random_number;
	
	// pick a random number betwen 0 and number of words in the "kind" array
	// taking the "floor" of the number returned - so 2.7 becomes 2
	random_number = Math.floor(Math.random() * words[kind].length);
	
	// return the word in that random position in the array
	word = words[kind][random_number];
	
	return word;
	
}

function makeName (version) {
	
	// passing the version number picks which construction to use
	
	var pac_name;
	
	// build the pac name based on preset formulas
	// if (version === 0) {
	//  pac_name = pickWord("verbs") + " the " + pickWord("adjectives") + " " + pickWord("nouns");
	//  }
	
	switch (version) {
		case 0: 
			pac_name = pickWord("political_stance") + " " + pickWord("political_stance_noun") + " " + "Party"
			break;

		case 1: 
			pac_name = "Put" + " " +  pickWord("put_nouns") + " " + pickWord("order") + " " + "Party"
			break;

		case 2: 
			pac_name = pickWord("single_phrase") + " " + "Party"
			break;

		case 3: 
			pac_name = pickWord("beginning") + " " + pickWord("general_nouns") + " " + "Party"
			break;

		case 4: 
			pac_name = pickWord("adjectives") + " " + pickWord("political_people") + " " + "Party";
			break;
                case 5:
			pac_name = "Tax" + " " + pickWord("tax_person") + " " + "Party";
			break;
                        
			
	}
	
	
	// put up spinner
	$('#words-container').html("<img src='images/spinner.gif'>&nbsp;");
	
	setTimeout(function () { 
		
			// put the words on the page
			// after one second
			
			$('#words-container').html(pac_name);

			// change the text to tweet out
			var tweet_html;
			tweet_html = "<span class='like-it'>Like it? Tweet it!</span><br><a href=\"http://twitter.com/share\" class=\"twitter-share-button\" data-url=\"http://wny.cc/Lv9rwO\" data-count=\"none\" data-text=\"'" + pac_name +"' - My random political party name generated at @afreecountry |\">Tweet</a><script type=\"text/javascript\" src=\"https://platform.twitter.com/widgets.js\"></script>";
			
			$('#twitter_button').html(tweet_html);
		
	}, 800);
	


}

function playGame() {
	
	// randomly pick a version and make the name
	
	// pick a random number between 0 and the number of versions
	var version = Math.floor( Math.random() * number_of_versions );
	
	makeName(version);
}
