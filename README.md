# ansible-lint

This is the rule-set I use for my ansible roles. By linting the roles and playbooks you get an standarized setup and use best practices.

## Setup

You need to have `ansible-lint` installed:

```bash
$ pip install ansible-lint
```

Check the rules out to a directory of your choice:

```bash
$ hub clone lxhunter/ansible-lint /usr/local/src/ansible-lint
# or
$ git clone https://github.com/lxhunter/ansible-lint.git /usr/local/src/ansible-lint
```

**Pro-Tip:** I use [fresh](https://freshshell.com) for this:

```bash
$ fresh lxhunter/ansible-lint . --file=/usr/local/src/ansible-lint
```

## Usage

Now you can lint your playbooks by doing:

```bash
# just my rules
$ ansible-lint -r /usr/local/src/ansible-lint/rules playbook.yml
# or for the standard rule and mine
$ ansible-lint -R -r /usr/local/src/ansible-lint/rules playbook.yml
# geek
```

## Rules

| **Code** | **Message** |
| --- |:---|
| **LX1** | **Playbook** |
| --- | |
| **LX2** | **Role** |
| --- | |
| **LX3** | **Task** |
| --- | |
| **LX4** | **General Module** |
| LX401 | Specific Modules should have owner, group and mode |
| --- | |
| **LX5** | **Specific Module** |
| LX501| Template Module - Template files should have the extension '.j2' |

## Testing

### Setup:

You need to have `nodemon` installed:

```bash
$ npm install
```

### Usage:

I used node for testing:

```bash
nodemon LX401
```

## Credits

* [Initial Idea from Will Thames](https://github.com/willthames/ansible-lint)
* [Learned a lot from shirou and his rules](https://github.com/shirou)

## Contribute

[Tutorial](http://kbroman.github.io/github_tutorial/pages/fork.html)

## Author

Author:: [Alexander Jäger](https://github.com/lxhunter)

Copyright 2018
