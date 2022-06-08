# %{PYRITE_RULE}

%{help.rule.summary}

```
<block type="ruleBlock">
	<mutation isOnGoingEvent="false"></mutation>
    <field name="EVENTTYPE">OnPlayerEarnedKill</field>
    <statement name="CONDITIONS">
        <block type="conditionBlock">
            <value name="CONDITION">
                <block type="Equals">
                    <value name="VALUE-0">
                        <block type="GetGamemodeScore">
							<value name="VALUE-0">
								<block type="GetTeamId">
									<value name="VALUE-0">
										<block type="EventPlayer"></block>
									</value>
								</block>
							</value>
						</block>
                    </value>
                    <value name="VALUE-1">
                        <block type="GetTargetScore" />
                    </value>
                </block>
            </value>
        </block>
    </statement>
	<statement name="ACTIONS">
        <block type="EndRound">
            <value name="VALUE-0">
                <block type="GetTeamId">
					<value name="VALUE-0">
						<block type="EventPlayer"></block>
					</value>
				</block>
            </value>
        </block>
    </statement>
</block>
```

### %{help.rule.typesofrule}

#### %{PYRITE_EVENT_ONGOING}

%{help.rule.ongoing}

#### %{ID_ARRIVAL_MODBUILDER_EVENT_ONPLAYERDIED}

%{help.rule.onplayerdied}

#### %{ID_ARRIVAL_MODBUILDER_EVENT_ONPLAYERDEPLOYED}

%{help.rule.onplayerdeployed}

#### %{ID_ARRIVAL_MODBUILDER_EVENT_ONPLAYERJOINGAME}

%{help.rule.onplayerjoingame}

#### %{ID_ARRIVAL_MODBUILDER_EVENT_ONPLAYERLEAVEGAME}

%{help.rule.onplayerleavegame}

#### %{ID_ARRIVAL_MODBUILDER_EVENT_ONPLAYEREARNEDKILL}

%{help.rule.onplayerearnedkill}

#### %{ID_ARRIVAL_MODBUILDER_EVENT_ONGAMEMODE}

%{help.rule.ongamemodeending}

#### %{ID_ARRIVAL_MODBUILDER_EVENT_ONMANDOWN}

%{help.rule.onmandown}

#### %{ID_ARRIVAL_MODBUILDER_EVENT_ONREVIVED}

%{help.rule.onrevived}

#### %{ID_ARRIVAL_MODBUILDER_EVENT_ONTIMELIMITREACHED}

%{help.rule.ontimelimitreached}

#### %{ID_ARRIVAL_MODBUILDER_EVENT_ONGAMEMODESTARTED}

%{help.rule.ongamemodestarted}

#### %{ID_ARRIVAL_MODBUILDER_EVENT_ONPLAYERIRREVERSIBLYDEAD}

%{help.rule.onplayerirreversiblydead}

#### %{ID_ARRIVAL_MODBUILDER_EVENT_ONVEHICLESPAWNED}

%{help.rule.onvehiclespawned}

#### %{ID_ARRIVAL_MODBUILDER_EVENT_ONVEHICLEDESTROYED}

%{help.rule.onvehicledestroyed}

#### %{ID_ARRIVAL_MODBUILDER_EVENT_ONPLAYERENTERVEHICLE}

%{help.rule.onplayerentervehicle}

#### %{ID_ARRIVAL_MODBUILDER_EVENT_ONPLAYEREXITVEHICLE}

%{help.rule.onplayerexitvehicle}

#### %{ID_ARRIVAL_MODBUILDER_EVENT_ONPLAYERENTERVEHICLESEAT}

%{help.rule.onplayerentervehicleseat}

#### %{ID_ARRIVAL_MODBUILDER_EVENT_ONPLAYEREXITVEHICLESEAT}

%{help.rule.onplayerexitvehicleseat}
