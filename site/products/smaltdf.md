# <Mark product="df" :size="40" /> smaltdf

<StageBadge />

**Small. Alternative. Frames.** Dataframes for smaltdb. Small and fast.

smaltdf is the second language for the smaltdb engine, next to [smaltql](/products/smaltql): a TypeScript dataframe API of frames,
expressions and method chains. Its API takes Narwhals as its reference.

It is a language, not a separate engine. smaltdf builds plans for the same plan layer smaltql uses, so a dataframe gets
smaltdb's optimizer, scans and storage. Use it from your own code, or interactively in smaltui and, later, smaltnb.


**Status:** in development, coming soon. Its design decisions are recorded in the repository, and it builds on
smaltdb's shared plan layer, which is in progress.

[Repository →](https://github.com/stenhoor/smaltdf)
