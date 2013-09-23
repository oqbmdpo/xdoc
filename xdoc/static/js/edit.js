var editor = angular.module('xdoc.editor', ['ui.ace', 'ngResource']);

editor.directive('resize', function ($window) {
    return function (scope) {
		var set_height = function(){
			scope.editor_style = {'height': $window.innerHeight-52+'px'};
		}
		set_height();
		angular.element($window).bind('resize', function() {
			scope.$apply(function () {
				set_height();
			});
		});
    };
});

editor.directive('markdown', function () {
	var converter = new Showdown.converter();
	return {
		restrict: 'AE',
		link: function (scope, element, attrs) {
			scope.$watch(attrs.ngModel, function (date) {
				if (date) {
					var html = converter.makeHtml(date);
					element.html(html);
				}
			});
		}
	};
});

editor.controller('AceCtrler', ['$scope', '$resource', function($scope, $resource) {
	var Draft = $resource('/draft/:draft_id', {draft_id:'@id'});
	$scope.draft = Draft.get({draft_id:"523942171d41c8aac0e3e1ce"});

	$scope.save = function() {
	};
}]);

