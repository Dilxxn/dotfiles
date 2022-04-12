if status is-interactive
    # Commands to run in interactive sessions can go here
end

### ALIASES ###
alias performance "sudo cpupower frequency-set --governor performance"
alias ondemand "sudo cpupower frequency-set --governor ondemand"
alias powersave "sudo cpupower frequency-set --governor powersave"

### CONFIGS ###

# Supress Welcome Message
set fish_greeting
