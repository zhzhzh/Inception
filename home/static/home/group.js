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

    $scope.teams = {
        'Team1': [],
        'Team2': []
    };

    $scope.team_index = 2;
    $scope.team_size = {
        'Team1': 0,
        'Team2': 0
    };

    function caclTeamMember(number) {
        var base = parseInt(number / $scope.team_index);
        var mod = number % $scope.team_index;

        for (var i = 0; i < $scope.team_list.length; i++) {
            var team = $scope.team_list[i];
            if (mod == 0) {
                $scope.team_size[team] = base;
            } else {
                $scope.team_size[team] = base + 1;
                mod = mod - 1
            }
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
    //$scope.attend_members = ["队长", "里克", "阿哥", "天天", "鞋魔", "蓝少", "哪吒", "蒂姆", "戈登", "球霸", "线裤",
    // "铁塔", "大派", "艾里克", "董", "亨利", "枭风", "小林", "球球", "弗莱明", "艾伦", "金吒", "木吒", "霉西"];

    caclTeamMember($scope.attend_members.length);

    $scope.member_team_mapping = {};

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
        //TODO

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
            { pos: '攻击型中场', dep: '防守型中场', exception: ['弗莱明', '里克'] },
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


        // top_star
        //var top_stars = un_grouped.filter(function(value) {
        //    return value.top_star;
        //});
        //
        //var top_star_num = top_stars.length;
        //var tmp_team_list = team_list.slice();
        //var team = undefined;
        //for (i = 0; i < top_star_num; i ++) {
        //    if (tmp_team_list.length == 0) {
        //        tmp_team_list = team_list.slice();
        //    }
        //    random_member_to_team(top_stars, tmp_team_list, un_grouped, tmp_teams);
        //}
        //
        //// 守门员
        //// 如果top_star分配不均并且守门员中有'阿哥',优先随机分配'阿哥'
        //var goal_keepers = un_grouped.filter(function(value) {
        //    return value.pos1 == '守门员';
        //});
        //var goal_keeper_num = goal_keepers.length;
        //
        //var top_star_min = Math.floor(top_star_num / team_number);
        //var team_star_unbalanced = [];
        //if (top_star_num % team_number != 0) {
        //    team_star_unbalanced = team_list.filter(function(value) {
        //        return tmp_teams[value]['top_star'] == top_star_min;
        //    });
        //}
        //
        //var has_a_ge = has_member(goal_keepers, 'nick_name', '阿哥');
        //tmp_team_list = team_list.slice();
        //if (team_star_unbalanced.length != 0 && team_star_unbalanced.length < goal_keepers.length) {
        //    if (has_a_ge) {
        //        team = team_star_unbalanced[random_choose(team_star_unbalanced.length)];
        //        member = attend_member_map['阿哥'];
        //        add_member_to_team(member, team, goal_keepers, team_star_unbalanced, un_grouped, tmp_teams);
        //        if (tmp_team_list.indexOf(team) > 0) {
        //            tmp_team_list.splice(tmp_team_list.indexOf(team), 1);
        //        }
        //    }
        //}
        //
        //if (team_star_unbalanced.length != 0) {
        //    tmp_team_list = team_star_unbalanced;
        //}
        //
        //length = goal_keepers.length;
        //for (i = 0; i < length; i++) {
        //    if (tmp_team_list.length == 0) {
        //        tmp_team_list = team_list.slice();
        //    }
        //    random_member_to_team(goal_keepers, tmp_team_list, un_grouped, tmp_teams);
        //}
        //
        //// 中后卫 cb
        //// 中后卫平均并随机分配到各组中，没有门将的组优先拿中后卫中的金亮
        //var cbs = un_grouped.filter(function(value) {
        //    return value.pos1 == '中后卫';
        //});
        //var cbs_num = cbs.length;
        //
        //var team_no_keeper = [];
        //tmp_team_list = team_list.slice();
        //if (goal_keeper_num < team_number) {
        //    team_no_keeper = team_list.filter(function(value) {
        //        return tmp_teams[value]['pos'].indexOf('守门员') < 0;
        //    });
        //
        //    var has_jin_liang = has_member(cbs, 'nick_name', '金亮');
        //    if (has_jin_liang) {
        //        member = attend_member_map['金亮'];
        //        team = team_no_keeper[random_choose(team_no_keeper.length)];
        //        add_member_to_team(member, team, cbs, team_no_keeper, un_grouped, tmp_teams);
        //        tmp_team_list.splice(tmp_team_list.indexOf(team), 1);
        //    }
        //}
        //
        //if (team_no_keeper.length > 0) {
        //    tmp_team_list = team_no_keeper;
        //}
        //
        //length = cbs.length;
        //for (i = 0; i < length; i++) {
        //    if (tmp_team_list.length == 0) {
        //        tmp_team_list = team_list.slice();
        //    }
        //
        //    random_member_to_team(cbs, tmp_team_list, un_grouped, tmp_teams);
        //}
        //
        //// 防守型中场 dm
        //// 防守型中场平均并随机分配到各组中，没有中卫的组优先拿铁军
        //var dms = un_grouped.filter(function(value) {
        //    return value.pos1 == '防守型中场';
        //});
        //var dms_num = dms.length;




        // Output:
        $scope.final_result = tmp_teams
    };

});