var submitApp = angular.module('submitApp', ['ngRoute']).
  config([
    '$httpProvider',
    '$interpolateProvider',
    '$routeProvider',
    '$locationProvider',
    function($httpProvider, $interpolateProvider, $routeProvider, $locationProvider) {
      // Configure the app to work with Django and Django templates
      $interpolateProvider.startSymbol('{$');
      $interpolateProvider.endSymbol('$}');
      $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
      $httpProvider.defaults.xsrfCookieName = 'csrftoken';
      $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

      // Configure routes
      $routeProvider
        .when('/', {
          templateUrl: 'static/translator/home.html',
          controller: 'formController'
        })
        .when('/translations', {
          templateUrl: 'static/translator/translations.html',
          controller: 'tableController'
        });

      // Make the routes nicer using HTML5 history api
      $locationProvider.html5Mode(true);
    }
  ]);

// Our form controller
submitApp.controller('formController', ['$scope', '$http', function($scope, $http) {
  $scope.formData = {};
  $scope.output = {
    lang: "N/A"
  };
  $scope.tableData = [];

  $scope.processForm = function() {
    $scope.output = {
      lang: "PROCESSING INPUT"
    };

    $http({
      method: 'POST',
      url: 'api/translate/',
      data: $.param($scope.formData)
    })
    .success(function(data) {
      // Set the dat for display to the user
      $scope.output = {
        translated_text: data.translated_text,
        lang: data.detected_language
      };
    });
  };
}]);

// Our table view controller
submitApp.controller('tableController', ['$scope', '$http', function($scope, $http) {
  $scope.translations = [];
  $http({
    method: 'GET',
    url: 'api/translations/'
  })
  .success(function(data) {
    console.log(data.translations);
    $scope.translations = data.translations;
  });
}]);
