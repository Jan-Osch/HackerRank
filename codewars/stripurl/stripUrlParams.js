function stripUrlParams(url, paramsToStrip) {
    const urlParamsRegexp = /([^?]*)\?(.*)/;

    if(!urlParamsRegexp.test(url)){
        return url;
    }

    const [whole, base, urlPart] = urlParamsRegexp.exec(url);
    const urlParams = urlPart.split('&');
    const strippedUrlParams = stripDuplicatesAndUnwanted(urlParams, paramsToStrip);

    return strippedUrlParams.length === 0
        ? base
        : `${base}?${strippedUrlParams.join('&')}`;

}
function stripDuplicatesAndUnwanted(urlParams, paramsToStrip) {
    let paramsToRemove = paramsToStrip || [];

    return urlParams.filter((param) => {
            const [paramName] = param.split('=');

            if (paramsToRemove.indexOf(paramName) === -1) {
                paramsToRemove.push(paramName);
                return true;
            }

            return false;
        }
    );
}

module.exports = stripUrlParams;


