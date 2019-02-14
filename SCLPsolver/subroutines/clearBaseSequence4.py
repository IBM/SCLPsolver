

def clearBaseSequence(base_sequence, NN, statData):
    basesActive = len(base_sequence['places'])
    basesToSave = min(max(round(statData.basesRate * NN), statData.minBases),statData.maxBases)
    numBasesToRemove =   basesActive -basesToSave
    if (numBasesToRemove > 0):
        rem = mod(basesActive, 2);
        ttf = [repmat([true, false], 1, (basesActive - rem)/2), true(rem)];
        orderedSequence = sort(MatrixAA.place);
        diffSeq = diff(orderedSequence);
        distances  = [diffSeq 0] + [0 diffSeq];
        x1 = distances(ttf);
        x2 = sort(x1);
        t=x2(numBasesToRemove);
        b = 1:basesActive;
        x3 = b(distances > t );
        x4 = b(distances == t );
        xx = length(x3)+length(x4) - basesToSave;
        if xx > 0
            x5 = randsample(x4,length(x4) - xx);
        else
            x5 = x4;
        end
        tosave = ismember(MatrixAA.place,[orderedSequence([x3,x5]), statData.N1, statData.N2]) | ttf;
        MatrixAA.place = MatrixAA.place(tosave);
        MatrixAA.matrix = MatrixAA.matrix(tosave);
