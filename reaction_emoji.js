class Reaction {
	constructor(uid, message = "") {
		this.user = uid;
		this.message = message.toLowerCase();
		this.reaction_emojis = [];
	}

	get reactions() {
		this.dateReactions();
		this.userReactions();
		this.messageReactions();
		return this.reaction_emojis;
	}

	dateReactions() {
		let curr_date = new Date();
		let ymd = `${curr_date.getMonth() + 1}-${curr_date.getDate()}`;

		let r = Math.floor(Math.random * 100);

		switch (ymd)
		{
			// New years Day
			case '1-01':
				this.reaction_emojis.push('🎉');
				break;

			// Valentines Day
			case '2-14':
				this.reaction_emojis.push('💘');

				if (this.user === '211258171094859776'
					|| this.user === '153673650929664000')
				{
					this.reaction_emojis.push('🌵');
				}
				break;

			// 4th of July
			case '7-04':

				let july_fourth_reaction = '🇺🇸';

				switch (r % 4)
				{
					case 0:
						july_fourth_reaction = '🔫';
						break;
					case 1:
						july_fourth_reaction = '🗽';
						break;
					case 2:
						july_fourth_reaction = '🦅';
					case 3:
						break;
					default:
						break;
				}

				this.reaction_emojis.push(july_fourth_reaction);
				break;

			// Thanksgiving
			case '11-26':
				this.reaction_emojis.push('🦃');
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
				let hanukkah_reaction = '🕎';

				switch (r % 5)
				{
					case 0:
						hanukkah_reaction = '🕎';
						break;
					case 1:
						hanukkah_reaction = '🕯️';
						break;
					case 2:
						hanukkah_reaction = '🥞';
						break;
					case 3:
						hanukkah_reaction = '🎁';
						break;
					case 4:
						hanukkah_reaction = '✡️';
						break;
				}
				this.reaction_emojis.push(hanukkah_reaction);
				break;

			// X-Mass
			case '12-25':
				this.reaction_emojis.push('🎄');
				break;

			// Boxing day
			case '12-26':
				this.reaction_emojis.push('📦');
				break;

			// New Years Eve
			case '12-31':
				this.reaction_emojis.push('🎉');
				break;

			default:
				break;
		}
	}

	messageReactions() {
		// React with "NICE" if the message contains 69
		if (this.message.includes("69"))
		{
			this.reaction_emojis.push('🇳');
			this.reaction_emojis.push('🇮');
			this.reaction_emojis.push('🇨');
			this.reaction_emojis.push('🇪');
		}

		if (this.message.includes("games") ||
			this.message.includes("gamz") ||
			this.message.includes('gamez'))
		{
			this.reaction_emojis.push('🎮');
			this.reaction_emojis.push('❓');
		}

		if (this.containsPen15())
		{
			this.reaction_emojis.push('🍆');
		}
	}

	userReactions() {
		switch (this.user)
		{
			// @UnitZer0
			case '211258171094859776':
				break;

			// @tjx1212
			case '214581352689958922':
				this.reaction_emojis.push('🦀');
				break;

			// @naps
			case '180729155829104640':
				this.reaction_emojis.push('🐒');
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
				this.reaction_emojis.push('💧');
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
	}

	containsPen15() {
		try
		{
			let index = this.message.indexOf("pen");

			if (index === -1)
				return false;

			let nums = this.message.substring(index + 3, this.message.length);

			if (eval(nums) === 15)
				return true;
			return false;
		}
		catch (e)
		{
			return false;
		}
	}
}

module.exports = Reaction;

