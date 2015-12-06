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

    $scope.add_team = function() {
        $scope.team_index = $scope.team_index + 1;
        var team = 'Team' + $scope.team_index;
        $scope.team_list.push(team);
        $scope.teams[team] = [];

    };

    $scope.attend_members = [];

});