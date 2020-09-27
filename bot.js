const Discord = require('discord.js');
const client = new Discord.Client();
const token = '';

client.login(token);

client.on('message', message => {
	// Add reaction based on who sent the message
	switch (message.author.id)
	{
		// @UnitZer0
		case '211258171094859776':
			break;

		// @tjx1212
		case '214581352689958922':
			message.react('🦀');
			break;

		// @naps
		case '180729155829104640':
			//message.react('🐒');
			break;

		// @ZaqueXIII
		case '153673650929664000':
			break;

		// @Blitztraum
		case '196317961890299904':
			break;

		// @Coop
		case '214861395211059201':
			break;

		// @JorJor The Dinosaur
		case '205043049024323584':
			break;

		// @Roost
		case '181914855706460160':
			break;

		// @Zega(Tyler)
		case '272442562177007619':
			break;

		// @Blahman
		case '220341843315916800':
			break;
		default:
			break;
	}

	let text = message.content.toLowerCase();

	// React with "NICE" if the message contains 69
	if (text.includes("69"))
	{
			message.react('🇳');
			message.react('🇮');
			message.react('🇨');
			message.react('🇪');
	}
	else if (text.includes("games") || text.includes("gamz") || text.includes('gamez'))
	{
			message.react('🎮');
			message.react('❓');
	} else if (text.includes("pen15"))
	{
		message.react('🍆');
	}
});
