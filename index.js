const { src, dest, task, series } = require("gulp");
const concat = require("gulp-concat");

const combineReadmes = () => {
	let directories = ["base", "graphs", "leetcode"];

	for (let i = 0; i < directories.length; i++) {
		directories[i] = `./${directories[i]}/**/*.md`;
	}

	return src(directories).pipe(concat("README.md")).pipe(dest("./"));
};

task("combine READMEs", combineReadmes);

function defaultTask() {
	series("combine READMEs")(combineReadmes);
}

exports.default = defaultTask;

defaultTask(() => {});
