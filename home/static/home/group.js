/**
 * Created by jzhang14 on 12/6/15.
 */

var app = angular.module('myApp', [
    'ngResource',
    'checklist-model'
    //'datatables',
    //'datatables.bootstrap',
    //'ui.bootstrap'
]);

app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});


app.factory('Members', function($resource) {
    return $resource('/data/members/');
});


app.controller('mainCtl', function($scope, Members) {
    $scope.members = Members.query();

    $scope.team_list = ['Team1', 'Team2'];

    $scope.jersey_files = {
        'r': 'Red_Jersey_Icon.jpg',
        'b': 'Blue_Jersey_Icon.jpg',
        'y': 'Yellow_Jersey_Icon.jpg'
    };

    $scope.teams = {
        'Team1': [],
        'Team2': []
    };

    $scope.team_index = 2;
    $scope.team_size = {
        'Team1': 0,
        'Team2': 0
    };

    $scope.has_blue = false;

    function caclTeamMember(number) {
        var base = parseInt(number / $scope.team_index);
        var mod = number % $scope.team_index;

        //for (var i = 0; i < $scope.team_list.length; i++) {
        //    var team = $scope.team_list[i];
        //    if (mod == 0) {
        //        $scope.team_size[team] = base;
        //    } else {
        //        $scope.team_size[team] = base + 1;
        //        mod = mod - 1
        //    }
        //}

        for (var i = 0; i < $scope.team_list.length; i++) {
            var team = $scope.team_list[i];
            $scope.team_size[team] = base;
        }

        var tmp_teams = $scope.team_list.slice();
        while (mod > 0) {
            var team_index = random_choose($scope.team_index);
            team = $scope.team_list[team_index];
            tmp_teams.splice(team_index, 1);
            $scope.team_size[team] = base + 1;
            mod = mod - 1;
        }


    }

    $scope.add_team = function() {
        $scope.team_index = $scope.team_index + 1;
        var team = 'Team' + $scope.team_index;
        $scope.team_list.push(team);
        $scope.teams[team] = [];
        $scope.team_size[team] = 0;
        caclTeamMember($scope.attend_members.length)
    };

    $scope.attend_members = [];

    //$scope.attend_members = ["陈老师", "文森特", "西门", "里克", "人品王", "天天", "华莱士", "姚俊", "线裤", "艾伦", "霉西",
    //    "球霸", "鞋魔", "哪吒", "徐老师", "阿哥", "铁军", "队长", "太郎", "华仔", "金亮", "小舅子", "蓝少", "枭风"];
    //$scope.attend_members = ["陈老师","本本","文森特","西门","里克","人品王","德里克","华莱士","线裤","球霸","鞋魔","阿哥","铁军","队长","小林","小P","弗莱明","戈登","枭风","蒂姆","哪吒"];

    caclTeamMember($scope.attend_members.length);

    $scope.member_team_mapping = {};

    $scope.reset = function() {
        for (var member in $scope.member_team_mapping) {
            $scope.member_team_mapping[member] = "";
        }
    };

    function removeFromTeams(name) {
        for (var key in $scope.teams) {
            var index = $scope.teams[key].indexOf(name);
            if (index != -1) {
                $scope.teams[key].splice(index, 1);
                return;
            }
        }
    }

    function addToTeam(name, team) {
        removeFromTeams(name);
        var team_list = $scope.teams[team];
        team_list.push(name);
    }


    $scope.$watch('attend_members', function(newValue, oldValue) {
        var newLength = newValue.length;
        var oldLength = oldValue.length;
        if(newLength > oldLength) {
            $scope.member_team_mapping[newValue[newLength-1]] = "";
            caclTeamMember(newLength);
        } else if(newLength < oldLength) {
            for(var i =0; i < oldLength; i++) {
                var name = oldValue[i];
                if (newValue.indexOf(name) == -1) {
                    delete $scope.member_team_mapping[name];
                    removeFromTeams(name);
                }
            }
            caclTeamMember(newLength);
        }
    }, true);

    $scope.$watch('member_team_mapping', function(newValue, oldValue) {
        var newSize = newValue.size;
        var oldSize = oldValue.size;

        if (newSize != oldSize) {
            return;
        }

        for (var i = 0; i < $scope.attend_members.length; i++) {
            var name = $scope.attend_members[i];
            if (newValue[name] != oldValue[name]) {
                if (newValue[name] == "") {
                    removeFromTeams(name);
                } else if (oldValue[name] == "") {
                    addToTeam(name, newValue[name]);
                } else {
                    addToTeam(name, newValue[name]);
                }

            }
        }
    }, true);

    function random_choose(max){
        var x = Math.floor(Math.random() * max);
        return x;
    }

    function add_member_to_team(member, team, member_list, team_list, un_grouped, tmp_teams) {
        if (member.top_star) {
            var star = "**"
        } else{
            var star = ''
        }
        console.log(star + member.nick_name + '|' + member.pos1 + '-->' + team);
        $scope.member_team_mapping[member.nick_name] = team;
        member_list.splice(member_list.indexOf(member), 1);
        team_list.splice(team_list.indexOf(team), 1);
        un_grouped.splice(un_grouped.indexOf(member), 1);
        tmp_teams[team]['members'].push(member);
        tmp_teams[team]['pos'].push(member.pos1);
        if (member.top_star) {
            tmp_teams[team]['top_star'] += 1;
        }
    }

    //function random_member_to_team(member_list, team_list, un_grouped, tmp_teams) {
    //    var member = member_list[random_choose(member_list.length)];
    //    var team = team_list[random_choose(team_list.length)];
    //
    //    add_member_to_team(member, team, member_list, team_list, un_grouped, tmp_teams);
    //}

    function has_member(member_list, key, value) {
        return member_list.filter(function(member) {
            if (key in member && member[key] == value) {
                return true;
            }
        }).length > 0;
    }

    function get_teams_no_full(team_list, tmp_teams) {
        return team_list.filter(function(value) {
            return tmp_teams[value]['members'].length < tmp_teams[value]['size'];
        });
    }

    function get_teams_without_pos(team_list, pos, tmp_teams) {
        var teams = get_teams_no_full(team_list, tmp_teams);
        return teams.filter(function(value) {
            if (pos == 'top_start') {
                return tmp_teams[value]['top_star'] == 0
            } else {
                return tmp_teams[value]['pos'].indexOf(pos) < 0
            }
        });
    }

    $scope.group_team = function() {

        // construct attend member map: nick_name => member object
        var attend_member_map = {};
        var length = $scope.members.length;
        for (var i = 0; i < length; i ++) {
            var member = $scope.members[i];
            if ($scope.attend_members.indexOf(member.nick_name) >= 0) {
                attend_member_map[member.nick_name] = member;
            }
        }

        var tmp_teams = {};
        var team_list = [];
        var grouped = [];
        for (var key in $scope.teams) {
            var team_members = $scope.teams[key];
            grouped = grouped.concat(team_members);
            team_list.push(key);

            tmp_teams[key] = {};
            tmp_teams[key]['size'] = $scope.team_size[key];

            tmp_teams[key]['members'] = [];
            tmp_teams[key]['pos'] = [];
            tmp_teams[key]['top_star'] = 0;

            length = team_members.length;
            for (i = 0; i < length; i++) {
                tmp_teams[key]['members'].push(attend_member_map[team_members[i]]);
            }
        }
        var team_number = team_list.length;

        var un_grouped = [];
        for (key in attend_member_map) {
            member = attend_member_map[key];
            if (grouped.indexOf(member.nick_name) < 0) {
                un_grouped.push(member);
            }

        }


        var grouping_conf = [
            { pos: 'top_star'},
            { pos: '守门员', dep: 'top_star', exception: ['阿哥'] },
            { pos: '中后卫', dep: '守门员', exception: ['金亮'] },
            { pos: '防守型中场', dep: '中后卫', exception: ['铁军'] },
            { pos: '攻击型中场'},
            //{ pos: '攻击型中场', dep: '防守型中场', exception: ['弗莱明', '里克'] },
            { pos: '特殊' },
            { pos: '前锋' },
            { pos: '边后卫' }
        ];

        var loop_length = grouping_conf.length;
        for(var loop_i = 0; loop_i < loop_length; loop_i++) {
            var conf = grouping_conf[loop_i];
            var pos = conf['pos'];

            var loop_members = un_grouped.filter(function (value) {
                if (pos == 'top_star') {
                    return value.top_star;
                } else {
                    return value.pos1 == pos;
                }
            });

            conf['number'] = loop_members.length;

            var round = 0;


            var loop_teams = undefined;

            while (loop_members.length > 0) {
                var member = undefined;
                var team = undefined;

                if (round == 0) {// logic for exception members
                    round += 1;
                    if ('dep' in conf) { // get teams have no dep pos
                        if (conf['dep'] == 'top_star') { // 获取top star分配不均的team
                            var top_star_num = grouping_conf[0]['number'];
                            if (top_star_num % team_number != 0) {
                                var top_star_min = Math.floor(top_star_num / team_number);
                                loop_teams = team_list.filter(function(value) {
                                    return tmp_teams[value]['top_star'] == top_star_min;
                                });
                            }
                        }
                        if (loop_teams == undefined) {
                            loop_teams = get_teams_without_pos(team_list, conf['dep'], tmp_teams);
                        }
                    } else { // get teams have no this pos
                        loop_teams = get_teams_without_pos(team_list, pos, tmp_teams)
                    }
                }

                if (loop_teams.length == 0) {
                    loop_teams = get_teams_without_pos(team_list, pos, tmp_teams);
                    if (loop_teams.length == 0) {
                        loop_teams = get_teams_no_full(team_list, tmp_teams);
                    }
                }
                team = loop_teams[random_choose(loop_teams.length)];

                if ('exception' in conf && conf['exception'].length > 0) {
                    for(var i = 0; i < conf['exception'].length; i++) {
                        if (has_member(loop_members, 'nick_name', conf['exception'][i])) {
                            member = attend_member_map[conf['exception'][i]];
                            break;
                        }
                    }
                }
                if (member == undefined) {
                    member = loop_members[random_choose(loop_members.length)]
                }

                add_member_to_team(member, team, loop_members, loop_teams, un_grouped, tmp_teams);
            }
        }

        // process Jersey
        if ($scope.attend_members.indexOf('蓝少') >= 0) {
            $scope.has_blue = true;
        }

        var jersey_list = ['b', 'y', 'r'];
        var tmp_team_list = $scope.team_list.filter(function(value) {return true});
        if ($scope.team_index <= 2) {
            jersey_list = ['b', 'y'];
        }

        if ($scope.has_blue) {
            var index = $scope.team_list.length;
            while (index--) {
                team = $scope.team_list[index];
                if (has_member(tmp_teams[team]['members'], 'nick_name', '蓝少')) {
                    tmp_teams[team]['jersey'] = 'b';
                    jersey_list.splice(jersey_list.indexOf('b'), 1);
                    tmp_team_list = $scope.team_list.filter(function(value) {return value != team});
                    break;
                }
            }
        }

        index = tmp_team_list.length;
        while (index--) {
            var jersey = jersey_list[random_choose(jersey_list.length)];
            jersey_list.splice(jersey_list.indexOf(jersey), 1);
            team = tmp_team_list[random_choose(tmp_team_list.length)];
            tmp_team_list.splice(tmp_team_list.indexOf(team), 1);
            tmp_teams[team]['jersey'] = jersey;
        }

        // Output:
        $scope.final_result = tmp_teams
    };

});