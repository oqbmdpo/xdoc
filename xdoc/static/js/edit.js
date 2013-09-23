var editor = angular.module('xdoc.editor', ['ui.ace', 'ngResource']);

editor.directive('ace', function () {
	if (angular.isUndefined(window.ace)) {
		throw new Error('ui-ace need ace to work... (o rly?)');
	}
	return {
		restrict: 'EA',
		require: '?ngModel',
		link: function (scope, elm, attrs, ngModel) {
			var options, opts, acee, session, onChange;

			acee = window.ace.edit(elm[0]);
			session = acee.getSession();

			onChange = function () {
				return function (e) {
					var newValue = session.getValue();
					if (newValue !== scope.$eval(attrs.value) && !scope.$$phase) {
						if (angular.isDefined(ngModel)) {
							scope.$apply(function () {
								ngModel.$setViewValue(newValue);
							});
						}
					}
				};
			};

			acee.renderer.setShowGutter(true);
			session.setUseWrapMode(true);

			acee.setTheme("ace/theme/textmate");
			session.setMode("ace/mode/markdown");
			acee.setFontSize(16);
			acee.setShowPrintMargin(false);

			if (angular.isDefined(ngModel)) {
				ngModel.$formatters.push(function (value) {
					if (angular.isUndefined(value) || value === null) {
						return '';
					}
					else if (angular.isObject(value) || angular.isArray(value)) {
						throw new Error('ui-ace cannot use an object or an array as a model');
					}
					return value;
				});

				ngModel.$render = function () {
					session.setValue(ngModel.$viewValue);
				};
			}

			// EVENTS
			session.on('change', onChange());
			elm.css('height', scope.editor_style['height']);
			acee.resize();

		}
	};
});

editor.directive('resize', function ($window) {
	return function (scope) {
		var set_height = function(){
			scope.editor_style = {'height': $window.innerHeight-38+'px'};
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

editor.controller('EditorCtrler', ['$scope', '$resource', function($scope, $resource) {
	var Draft = $resource('/draft/:draft_id', {draft_id:'@id'});
	$scope.draft = Draft.get({draft_id:"524050391d41c8299c1e5e10"});

	$scope.save = function() {
	};
}]);
