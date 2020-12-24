const Discord = require('discord.js');
const client = new Discord.Client();
const token = '';

client.login(token);

function containsPen15(str) {
	let index = str.indexOf("pen");

	if (index === -1)
		return false;

	let nums = str.substring(index + 3, str.length);

	if (eval(nums) === 15)
		return true;
	return false;
}

client.on('message', message => {
	let curr_date = message.createdAt;
	let ymd = `${curr_date.getMonth() + 1}-${curr_date.getDate()}`;

	switch (ymd)
	{
		// Thanksgiving
		case '11-26':
			message.react('🦃');
			break;

		// X-Mass
		case '12-25':
			message.react('🎄');
			break;

		// Boxing day
		case '12-26':
			message.react('📦');
			break;

		// New Years Eve
		case '12-31':
			message.react('🎉');
			break;

		// Hanukkah 2020 Dates
		case '12-10':
		case '12-11':
		case '12-12':
		case '12-13':
		case '12-14':
		case '12-15':
		case '12-16':
		case '12-17':
		case '12-18':
			let r = Math.floor(Math.random() * 100) % 5;
			let emoji = '🕎';

			switch (r)
			{
				case 0:
					emoji = '🕎';
					break;
				case 1:
					emoji = '🕯️';
					break;
				case 2:
					emoji = '🥞';
					break;
				case 3:
					emoji = '🎁';
					break;
				case 4:
					emoji = '✡️';
					break;
			}
			message.react(emoji);
			break;

		default:
			break;
	}

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
			message.react('🐒');
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
			message.react('🚚');
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

		// @GaryArk3443
		case '388449127333232642':
			break;

		// @A Single Neuron
		case '187039157426585600':
			break;

		// @lucii
		case '424766351622537216':
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

	if (text.includes("games") ||
		text.includes("gamz") ||
		text.includes('gamez'))
	{
			message.react('🎮');
			message.react('❓');
	}

	if (containsPen15(text))
	{
		message.react('🍆');
	}
});
