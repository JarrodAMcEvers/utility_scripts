# story [number]
# devs [dev1] [dev2] [dev3] etc
# ci message for commit
# cia message for commit

# preview message
function ms{
	"#$($env:story_number) - [$($env:devs_working)]"
}

# story number
function story($story_number){ $env:story_number = $story_number }

# developers working on the story
function devs{ $env:devs_working = $args}

# git commit for commited files only
function ci{ $msg = "#$($env:story_number) - $($args) [$($env:devs_working)]" ; git commit -m $msg}

# git commit on everything
function cia{ $msg = "#$($env:story_number) - $($args) [$($env:devs_working)]" ; git add -A ; git commit -m $msg}