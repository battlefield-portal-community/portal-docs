# %{ID_ARRIVAL_BLOCK_SORTEDARRAY}

%{help.sortedarray.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_ARRAY}
2. %{PYRITE_TYPE_NUMBER}

    %{help.common.contexts.rank}

### %{help.common.output}

-   %{PYRITE_TYPE_ARRAY}

```
<block type="SortedArray">
    <value name="VALUE-0">
        <block type="AllPlayers"></block>
    </value>
    <value name="VALUE-1">
        <block type="GetGamemodeScore">
            <value name="VALUE-0">
                <block type="CurrentArrayElement"></block>
            </value>
        </block>
    </value>
</block>
```