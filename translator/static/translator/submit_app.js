// Configure the app to work with Django and Django templates
var submitApp = angular.module('submitApp', []).
  config([
    '$httpProvider',
    '$interpolateProvider',
    function($httpProvider, $interpolateProvider) {
      $interpolateProvider.startSymbol('{$');
      $interpolateProvider.endSymbol('$}');
      $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
      $httpProvider.defaults.xsrfCookieName = 'csrftoken';
      $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }
  ]);

// Our form controller
submitApp.controller('formController', ['$scope', '$http', function($scope, $http) {
  $scope.formData = {};
  $scope.output = {
    lang: "N/A"
  };

  $scope.processForm = function() {
    $scope.output = {
      lang: "PROCESSING INPUT"
    };

    $http({
      method: 'POST',
      url: 'translate/',
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
