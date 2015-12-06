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

    $scope.group_team = function() {
        //TODO
    };

});