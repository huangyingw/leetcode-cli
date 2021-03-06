'use strict';
var util = require('util');

var _ = require('underscore');
var childProcess = require('child_process');

var h = require('../helper');
var file = require('../file');
var chalk = require('../chalk');
var icon = require('../icon');
var log = require('../log');
var config = require('../config');
var core = require('../core');
var session = require('../session');

const cmd = {
  command: 'show [keyword]',
  aliases: ['view', 'pick'],
  desc:    'Show question',
  builder: function(yargs) {
    return yargs
            .option('a', {
                alias: 'all',
                type: 'boolean',
                default: false,
                describe: 'show all questions'
            })
      .option('c', {
        alias:    'codeonly',
        type:     'boolean',
        default:  false,
        describe: 'Only show code template'
      })
      .option('e', {
        alias:    'editor',
        type:     'string',
        describe: 'Open source code in editor'
      })
      .option('g', {
        alias:    'gen',
        type:     'boolean',
        default:  false,
        describe: 'Generate source code'
      })
      .option('l', {
        alias:    'lang',
        type:     'string',
        default:  config.code.lang,
        describe: 'Programming language of the source code',
        choices:  config.sys.langs
      })
      .option('o', {
        alias:    'outdir',
        type:     'string',
        describe: 'Where to save source code',
        default:  '.'
      })
      .option('q', core.filters.query)
      .option('t', core.filters.tag)
      .option('x', {
        alias:    'extra',
        type:     'boolean',
        default:  false,
        describe: 'Show extra question details in source code'
      })
      .positional('keyword', {
        type:     'string',
        default:  '',
        describe: 'Show question by name or id'
      })
      .example(chalk.yellow('leetcode show 1'), 'Show question 1')
      .example(chalk.yellow('leetcode show 1 -gx -l java'), 'Show question 1 and generate Java code')
      .example(chalk.yellow('leetcode show 1 -gxe'), 'Open generated code in editor')
      .example('', '')
      .example(chalk.yellow('leetcode show'), 'Show random question')
      .example(chalk.yellow('leetcode show -q h'), 'Show random hard question')
      .example(chalk.yellow('leetcode show -t google'), 'Show random question from Google (require plugin)');
  }
};

function genFileName(problem, opts) {
  const path = require('path');
  const params = [
        problem.fid,
        problem.slug,
    h.langToExt(opts.lang)
  ];

    return path.join(opts.outdir, params.join('.').replace(/\.+/g, '.'));
}

function showProblem(problem, argv) {
  const taglist = [problem.category]
    .concat(problem.companies || [])
    .concat(problem.tags || [])
    .map(x => h.badge(x, 'blue'))
    .join(' ');
  const langlist = problem.templates
    .map(x => h.badge(x.value, 'yellow'))
    .sort()
    .join(' ');

  let code;
  const needcode = argv.gen || argv.codeonly;
  if (needcode) {
    const template = problem.templates.find(x => x.value === argv.lang);
    if (!template) {
      log.fail('Not supported language "' + argv.lang + '"');
      log.warn('Supported languages: ' + langlist);
      return;
    }

    const opts = {
      lang: argv.lang,
      code: template.defaultCode,
      tpl:  argv.extra ? 'detailed' : 'codeonly'
    };
    code = core.exportProblem(problem, opts);
  }

  let filename;
  if (argv.gen) {
    file.mkdir(argv.outdir);
    filename = genFileName(problem, argv);

        if (!file.exist(filename)) {
    file.write(filename, code);
    }
  } else {
    if (argv.codeonly) {
      log.info(chalk.yellow(code));
      return;
    }
  }

    log.printf('[%d] %s %s', problem.fid, problem.name,
      (problem.starred ? chalk.yellow(icon.like) : icon.empty));
  log.info();
  log.info(chalk.underline(problem.link));
  if (argv.extra) {
    log.info();
    log.info('Tags:  ' + taglist);
    log.info();
    log.info('Langs: ' + langlist);
  }

  log.info();
  log.printf('* %s', problem.category);
    log.printf('* %s (%.2f%%)', h.prettyLevel(problem.level), problem.percent);

  if (filename)
    log.printf('* Source Code:       %s', chalk.yellow.underline(filename));
  if (problem.totalAC)
    log.printf('* Total Accepted:    %s', problem.totalAC);
  if (problem.totalSubmit)
    log.printf('* Total Submissions: %s', problem.totalSubmit);
  if (problem.testable && problem.testcase)
    log.printf('* Testcase Example:  %s', chalk.yellow(util.inspect(problem.testcase)));

  log.info();
  log.info(problem.desc);
}

cmd.handler = function(argv) {
  session.argv = argv;
    if (argv.all) {
        core.getProblems(function(e, problems) {
            if (e) return log.fail(e);

            for (let problem of problems) {
                core.getProblem(problem.fid, function(e, problem) {
      if (e) return log.fail(e);
      showProblem(problem, argv);
    });
            }
      });
        return;
    }

    if (argv.keyword.length > 0) {
        // show specific one
        core.getProblem(argv.keyword, function(e, problem) {
        if (e) return log.fail(e);
        showProblem(problem, argv);
      });
  }
};

module.exports = cmd;
