function songs(arg) {
    let rmLoop = arg.shift()
    let typeSongs = arg.pop()

    for (const el of arg) {
        let [type, name] = el.split('_')

        if (typeSongs === type || typeSongs == 'all') {
            console.log(name)
        }
    }
}

// songs([2, 'like_Replay_3:15', 'ban_Photoshop_3:48', 'all'])