/**
 * Created by jzhang14 on 12/6/15.
 */

var app = angular.module('myApp', [
    'ngResource'
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

    $scope.teams = {
        'T1': [],
        'T2': []
    }


});