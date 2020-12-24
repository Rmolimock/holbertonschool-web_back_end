// comment
export default function cleanSet(set, startString) {
	let s = '';
	if (startString !== '' && typeof (startString) === 'string') {
		set.forEach((val) => {
			if (val.includes(startString)) s = s.concat(`-${val.replace(startString, '')}`);
		});
		s = s.substring(1);
	}
	return s;
}
