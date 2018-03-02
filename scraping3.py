from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=video%20cards&recaptcha=pass'

# Descomentar, tuve que poner la respuesta en duro porque bloqueaban
#uClient = uReq(my_url)
#page_html = uClient.read()

page_html = '''
<!DOCTYPE HTML>
<html lang="en">
<head>
<script src="//assets.adobedtm.com/d2f967b83a0c92b19d9b572545fdbdc3d591f6f5/satelliteLib-389760a7bc4573d6b081d36f6782b59f3c8ffb54.js"></script>
	<title>Graphics Cards and Video Cards - Newegg.com</title>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<meta name="referrer" content="always">
	<meta name="keywords" content="Graphics Cards, Video Cards">
	<meta name="description" content="Shop a wide selection of Video Graphics Cards from EVGA, Gigabyte, MSI &amp; more! Newegg offers the best prices, fast shipping and top-rated customer service!">
	<meta property="og:image" content="https://c1.neweggimages.com/WebResource/Themes/2005/Nest/logo_424x210.png">
	<meta property="og:description" content="Shop a wide selection of Video Graphics Cards from EVGA, Gigabyte, MSI &amp; more! Newegg offers the best prices, fast shipping and top-rated customer service!">
	<link rel="alternate"  media="only screen and (max-width: 640px)"  href="https://m.newegg.com/categories/38/video-cards-video-devices"  />
	<meta name="google-translate-customization" content="d08b8c829bab9a46-ac914e23c0a3607a-g7fba27d07436db8a-e">
	<meta name="language" content="english">
	<meta name="copyright" content="&copy; 2000-2018 Newegg Inc.">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="robots" content="index,follow">
	<link rel="canonical" href="https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38">
	<link rel="shortcut icon" type="image/x-icon" href="//c1.neweggimages.com/WebResource/Themes/2005/Nest/Newegg.ico">
	<link rel="stylesheet" type="text/css" href="//c1.neweggimages.com/WebResource/Themes/2005/CSS/USA/WWWShared.14164.0.min.css"/>
	<link rel="stylesheet" type="text/css" href="//c1.neweggimages.com/WebResource/Themes/2005/CSS/USA/WWWStorePages2016.14164.2.min.css"/>
	<script type="text/javascript">var nebs = nebs||{};nebs.errors = [];window.onerror = function(){nebs.errors.push(arguments);return true;};</script>
	<script type="text/javascript" src="//c1.neweggimages.com/WebResource/Scripts/USA/NeweggJS/NEG.0.2.4.js" crossorigin="anonymous"></script>
	<script type="text/javascript">(function(NEG){if(NEG && NEG.setVersion){NEG.setVersion([{"module":"Biz.Cookie","version":"12376"},{"module":"Biz.Storage","version":"13637.4"},{"module":"Biz.InvodoVideo","version":"9792"},{"module":"Biz.Items","version":"9792"},{"module":"Biz.Resource","version":"9792"},{"module":"Biz.SearchKeywords","version":"9792"},{"module":"NEG.Utility.QueryStringBuilder","version":"11847"},{"module":"NEG.Widget.History","version":"9792"},{"module":"NEG.Widget.ImageZoomer","version":"13375.1"},{"module":"NEG.Widget.Mask","version":"10825"},{"module":"NEG.Widget.RangeSlider","version":"12739.0"},{"module":"NEG.Widget.Scroll","version":"9792"},{"module":"NEG.Widget.Viewport","version":"9792"},{"module":"NEG.Widget.Popup","version":"11629"},{"module":"Widget.Switch","version":"11315"},{"module":"NEG.Widget.AutoConfigurator","version":"10825.1"},{"module":"NEG.Widget.FilterManager.Model","version":"10520"},{"module":"NEG.Widget.FilterManager.View","version":"10520"},{"module":"NEG.Widget.PropertyManager.Model","version":"10520.2"},{"module":"NEG.Widget.PropertyManager.ViewManager","version":"10520.2"},{"module":"Utility.Cookie","version":"11621.1"},{"module":"Utility.JQuery","version":"12376"},{"module":"NEG.ThirdParty.JQuery","version":"12376"},{"module":"Biz.Common.Popup","version":"13760.1"},{"module":"Biz.Common.RecentlyView2016","version":"13025.1"},{"module":"Biz.Common.RecentlyView2012","version":"13025.1"},{"module":"Biz.Product.ProductPersonalization","version":"14254.e0"},{"module":"Biz.Product.MiniFeatures","version":"13025.0"}]);}})(NEG);</script>
	<script type="text/javascript" src="//c1.neweggimages.com/WebResource/Scripts/USA/TP_jQueryPlugin/jquery-1.10.2.min.js?purge=1" crossorigin="anonymous"></script>
	<script type="text/javascript">if(!(typeof jQuery==='undefined')){if($===jQuery){jQuery.noConflict();}}</script>
	<script type="text/javascript">if(sessionStorage.isEDUip_Newegg!="false" && sessionStorage.isEDUip_Newegg!="true"){jQuery.ajax({type: "GET",async: true,timeout:3000,url: "https://www.newegg.com/Common/Ajax/CheckEDUByIP.aspx",success: function(response){if (response) {var str = response.toString();if (str && str.indexOf("true") > -1) {window.isEDUip = "true";} else {window.isEDUip = "false";}} else {window.isEDUip = "false";}sessionStorage.isEDUip_Newegg=window.isEDUip;}});}else{window.isEDUip=sessionStorage.isEDUip_Newegg;}</script>
	<script type="text/javascript" src="//c1.neweggimages.com/WebResource/Scripts/USA/TP_jQueryPlugin/jquery-migrate-1.2.1.min.js" crossorigin="anonymous"></script>
	<script type="text/javascript" src="//c1.neweggimages.com/WebResource/Scripts/USA/TP_jQueryPlugin/popup.1.2.4.js" crossorigin="anonymous"></script>
	<script type="text/javascript">var nt_serverName="E11WEB07";var CANSite="//www.newegg.ca";var DOMAIN_NAME=".newegg.com",DOMAIN_TEXT="Newegg.com";if(!window["Web"]){Web={};};Web["Config"]={Environment:{Url:{WWW:'https://www.newegg.com/',Shopper:'https://secure.newegg.com/',Secure:'https://secure.newegg.com/',Content:'https://www.newegg.com/',CDN:'https://www2.newegg.com/',HttpCache:'//c1.neweggimages.com/WebResource/',HttpsCache:'//c1.neweggimages.com/WebResource/',HttpJSCache:'//c1.neweggimages.com/WebResource/',HttpsJSCache:'//c1.neweggimages.com/WebResource/',Local:'/WebResource/',Language:'en-US'},SSLPage:{Login:'https://secure.newegg.com/NewMyAccount/AccountLogin.aspx?nextpage=https%3a%2f%2fwww.newegg.com%2fStore%2fCategory.aspx%3fCategory%3d38%26Tpk%3dvideo%2520cards%26recaptcha%3dpass',Loginout:'https://secure.newegg.com/NewMyAccount/AccountLogout.aspx',MyAccountIndex:'https://secure.newegg.com/NewMyAccount/Index.aspx',Shoppingcart:'https://secure.newegg.com/Shopping/ShoppingCart.aspx',AddTocart:'https://secure.newegg.com/Shopping/AddToCart.aspx',ActivePoint:'https://secure.newegg.com/NewMyAccount/ActivePoints.aspx',NewMyAccountAutoNotify:'https://secure.newegg.com/NewMyAccount/AutoNotify.aspx'},Path:{Images:'Themes/2005/Nest/',Scripts:'Scripts/',Css:'Themes/2005/CSS/'},Cookies:{EnableCookieNameMapping:1},AutoFillBold:{Enable:true,UseContentPage:true},IE11VersionUpgrade:true,SwitchCountrySelectorPopup:true,NeweggGlobalUrl:'http://promotions.newegg.com/international/global/index.html',WWWPage:{B2BSepEnable: false,IsHomepage: false,IsProductList: false,IsNewStoreAndList: false,IsDailyDealStore: false,IsSubcategory: false,NeweggGlobalStore:'https://www.newegg.com/Newegg-Global/Store',ProductListEnableRightSide:true},SyncShoppingCart:{MinicartServiceEnable:true,ItemPriceLink:'https://secure.newegg.com/Common/Ajax/MiniCartService.aspx',ItemDetailLink:'https://secure.newegg.com/Common/Ajax/MiniCartService.aspx?IsDetail=true',}},CookieMapping:{'NV_CONFIGURATION':['.newegg.com',86400000,'',false],'NV_PRDLIST':['.newegg.com',86400000,'',false],'NV_ADVSEARCHOPEN':['.newegg.com',86400000,'',false],'NV_CUSTOMERLOGIN':['.newegg.com',0,'',true],'NV_AFFILIATECUSTOMER':['.newegg.com',604800,'',false],'NV_HBXCM':['.newegg.com',86400000,'',false],'NV_ADVSEARCHOPEN':['.newegg.com',86400000,'',false],'NV_CONTACTUS_COOKIE':['.newegg.com',86400000,'',false],'NV_VENDOR_NEWS_LIST':['.newegg.com',86400000,'',false],'CELL_PHONE_COMBO':['.newegg.com',86400000,'',false],'CELL_PHONE_PACKAGE':['',86400000,'',false],'NV_THANKYOUTRACKCOOKIE':['.newegg.com',86400,'',false],'NV_CDICOOKIE':['.newegg.com',10800,'',false],'NV_CUSTOMERREVIEWCOOKIE':['',86400000,'',false],'NV_GOOGLE_ANALYTICS':['.newegg.com',2592000,'',false],'NV_DVINFO':['.newegg.com',0,'',false],'NV_THIRD_PARTY':['.newegg.com',2592000,'',false],'NV_NEWGOOGLE_ANALYTICS':['.newegg.com',2592000,'',false],'NV_CUSTOMERLOGININTERNALUSER':['.newegg.com',0,'',false],'NV_B2BCUSTOMERLOGIN':['.newegg.com',0,'',true],'NV_TESTCOOKIE':['.newegg.com',0,'',false],'NV_MyNeweggModule':['.newegg.com',2592000,'',false],'AB':['.newegg.com',0,'',false],'NV_SURVEY':['.newegg.com',2592000,'',false],'NV_CERTONA':['.newegg.com',86400,'',false],'NV_FV':['.newegg.com',0,'',false],'NV_WISHLIST':['.newegg.com',2592000,'',false],'NV_COUNTRY':['.newegg.com',2592000,'',false],'NV_OTHERINFO':['.newegg.com',0,'',false],'NVTC':['.newegg.com',2592000,'',false],'NV_RECENTLYVIEWEDS':['.newegg.com',2592000,'',false],'NV_SPT':['.newegg.com',0,'',false],'NV_NEWEGGCOOKIE':['.newegg.com',0,'',false],'NV_LOCALSTORAGE':['.newegg.com',86400000,'',false],'NV_NID':['.newegg.com',2592000,'',false]},SiteCookieInfo:{bizUnit:"USA",enableReformattedCookie:true,writeReformattedCookie:true},NVTC:{UTMAExpireTime:30,SiteID:"0001"},SiteCatalyst:{Enable:true},recaptchaKey:"6Ld0av8SAAAAAA_bWcLCPqT109QEfdRp0w50GCsq"};Web["Lang"]={"account":"Account Settings","activity":"Activity","addNewVehicle":"Add Vehicle","addToCartErrorMessage":"Some items cannot be added to cart.","afterInstantSavings":"after {0}{1} instant savings","anyEngine":"Any Engine","anyTrim":"Any Trim","autoEngine":"Engine","autoMake":"Make","autoModel":"Model","autoPartsFor":"AUTO PARTS FOR","autoPartsFor2016":"Select Vehicle:","autoTrim":"Trim","autoYear":"Year","buyTogetherAndSave":"Buy Together and Save","by":"By","close":"close","close1":"Close","confirmCustomerEmailAddressInvalid":"- The Confirm Email address you entered is invalid.","cons":"Cons:","correctErrorDescription":"Please correct these error(s) and re-submit","createABundle":"Create a Bundle","currencyCode":"$","customerEmailAddressInvalid":"- The Email address you entered is invalid.","customerProductReview":"Customer Product Review","dateAndTime":"Date/Time","defaultTextInSearchBox":"Keywords, Model # or Item #","defaultWishListName":"Enter new list name here","deleteGarageErrorMessage":"A network error has occurred. Please try again to remove this vehicle.","deleteGarageErrorMessageTitle":"Error","deliveryDate":"Delivery date","destination":"Destination","details":"Details","eggReviews":"{0} egg reviews","emailAddress":"Email Address","emailAddressInvalid":"Your email address is invalid","emailAddressNotMatch":"- Email addresses you input do not match.","emailFieldEmpty":"Your email field is empty","emptyShoppingCart":"Empty Shopping Cart","enterEmail":"Enter your e-mail","enterNewVehicle":"Enter a New Vehicle","enterTheKeyword":"Enter the Keyword","expectedDelivery":"Expected delivery","expiresSoon":"Expires Soon","findPartsFor":"Find Parts for","freeShipping":"Free Shipping","freeShippingBracketMark":"Free Shipping ({0})","freeShippingExclamationMark":"Free Shipping","iframeForLayout":"iframe for layout","in":"in","inputRequired":"More Information Required","inputZipCode":"Please input zip code and continue","itemNumber":"Item Number","items":"0 Items","items1":"Item(s)","items2":"Items","length":"Length:","limitMessageDescription":"- You have exceeded the 1000 characters limit in 'Message' box.","limitTextDescription":"- You have exceeded the {0} characters limit in '{1}' box.","loading":"LOADING...","location":"Location","login":"Login","login2011":"Log in or Register","loginSingnel":"Log in","logOut":"log out","manufacturerVideo":"Manufacturer Video","marketplaceSeller":"Marketplace Seller","messageInvalid":"- The Message you entered is invalid.","myAccount":"My Account","newegg":"newegg","next":"Next &raquo;","no":"No","none":"None","noOrderRecord":"No Order in the last 15 days.","notAvailable":"N/A","notFoundItemDescription":"Sorry! We have found 0 items that match your search criteria \"{0}\".","notFoundVideoDescription":"Sorry! We have found 0 video.","on":"{0} on {1}","or":"or","otherThoughts":"Other Thoughts:","ownership":"- Ownership:","packageNumber":"Package number","password":"Password","pleaseChooseAOption":"Please choose a {0}","pleaseInputValue":"- Please Input value -","pleaseSelect":"- Please select -","prev":"&laquo; Prev","pros":"Pros:","qASuccessfullySubscribed":"You've successfully subscribed this question !","qASuccessfullyUnSubscribed":"You've successfully unsubscribed this question !","qty":"Qty","qtyBoxDescription":"Please enter a numeric value in the QTY box.","quickAdddeactivated":"# is a deactivated item. Please try again with another item.","quickAddEmptyListError":"Unable to add any items to the shopping cart. Reason: Empty List.","quickAddInvalidError":"Unable to add any items to the shopping cart. Reason: Invalid item(s).","quickAddItemsAcademicError":"# is an academic edition software. You cannot use item number to add this to shopping cart or To-Buy list.","quickAddItemsBuyAlongError":"# is part of a combo deal and cannot be sold separately.  Please try again with another item.","quickAddMorethan5Items":"Your input has resulted in more than 5 items. To narrow down your search, please try again with another Item Number or Mfr. Model Number.","quickAddNotFound":"# is not found.Please review the number and try again.","quickAddoutofstock":"We are sorry. This item is currently out of stock.","quickAddPleaseSelectone":"Please select one:","quickAddSelectitems":"# is associated to multiple items.","quickAddShortage":"Currently only # in stock.","rating":"Rating + {0}","ratingIcon":"rating rating-{0}","readEggReviews":"Read {0} egg reviews","register":"Register","removeItem":"Remove item","requestErrorDescription":"Your request cannot continue because of the following error(s)","reviewedBy":"Reviewed By:","reviewersGaveThisItem":"{0} reviewers gave this item {1} of 5","sampleItemNumber":"i.e. N82E16800996056","sampleItemNumberB2B":"i.e. 9B-00-996-056","saveerror":"Save error please try agian.","saveUpTo":"Save up to $","saveWishListEmpty":"Unable to save any items for later. Reason: Empty List.","saveWishListInvalid":"Unable to save any items for later. Reason: Invalid item(s).","searchKeywords":"(keywords)","searchWithin":"Search Within","seeTerms":"See Terms","select":"Select...","selectACarrier":"- Please select a carrier -","selectanItem":"Select an Item","selectAPhone":"- Please select a phone -","selectAPlan":"- Please select a plan -","selectMaxItems":"You may select only up to 5 items at a time to compare","selectMore":"Select one more item to compare","selectYesOrNo":"Please select YES or NO.","serviceType":"Service type","shipDate":"Ship date","shippedByNewegg":"Shipped by Newegg","shippingInformation":"Shipping Information","shippingLimitations":"Shipping Limitations","shippingRestrictions":"Shipping Restrictions","shoppingCartwithItems":"Shopping Cart with Items","smartSortHelpMsg":"Try the new smart sort tool","status":"Status","studentProgram":"Student Program Eligibility","techLevel":"Tech Level:","textSearchTerms":"Text Search Terms:","thisFit":"This fits","thisNotFit":"This doesn't fit","trackingNumber":"Tracking number","uploadBy":"Upload By:","userNameInvalid":"- The Name you entered is invalid.","videoContest":"Video Contest","viewShoppingCart":"View Shopping Cart","warrantyInfo":"Warranty Info","weight":"Weight","whenYouPurchaseTheseItemTogether":"when you purchase these items together","wishlistEmptyName":"Please enter a new list name.","wishlistError":"System error, please try again.","wishlistexisting":"The title has been used, please use another one.","yes":"Yes","yourOpinionisTooLong":"Your opinion is too long.","yourPrice":"Your Price:"};</script>
	<script type="text/javascript" src="//c1.neweggimages.com/WebResource/Scripts/USA/Common/GgewenFramework.v1.w.13720.em.6.js" crossorigin="anonymous"></script>
	<script type="text/javascript" src="//c1.neweggimages.com/WebResource/Scripts/USA/Common/WebApplication.v1.w.14134.0.js" crossorigin="anonymous"></script>
	<script type="text/javascript" src="//c1.neweggimages.com/WebResource/Scripts/USA/Common/PageDisplayLib.v1.w.14072.0.js" crossorigin="anonymous"></script>
	<script type="text/javascript" src="//c1.neweggimages.com/WebResource/Scripts/USA/Common/AutoFilledKeywords.v1.w.14074.1.js" crossorigin="anonymous"></script>
	<script type="text/javascript" src="//c1.neweggimages.com/WebResource/Scripts/USA/Common/BizCommon.v1.w.14247.1.js" crossorigin="anonymous"></script>
	<script type="text/javascript" src="//c1.neweggimages.com/WebResource/Scripts/USA/Common/json2.min.js" crossorigin="anonymous"></script>
	<script type="text/javascript" src="//c1.neweggimages.com/WebResource/Scripts/USA/Common/swfobject.v1.5.js" crossorigin="anonymous"></script>
	<script type="text/javascript" src="//c1.neweggimages.com/WebResource/Scripts/USA/Common/swiper.min.3.4.2.js" crossorigin="anonymous"></script>
	<script type="text/javascript" src="//c1.neweggimages.com/WebResource/Scripts/USA/WWW/SearchPanel2016.v1.w.14164.0.js" crossorigin="anonymous"></script>
	<script type="text/javascript" src="//c1.neweggimages.com/WebResource/Scripts/USA/WWW/ProductList2016.v1.w.13660.1.js" crossorigin="anonymous"></script>
	<script type="text/javascript" src="//c1.neweggimages.com/WebResource/Scripts/USA/WWW/AutoConfiguratorStripe2016.v1.w.13382.0.js" crossorigin="anonymous"></script>
	<script type="text/javascript" src="//c1.neweggimages.com/WebResource/Scripts/USA/WWW/Store.v1.w.13308.11.js" crossorigin="anonymous"></script>
	
<!-- Begin Monetate ExpressTag Sync v8.1. Place at start of document head. DO NOT ALTER. -->
<script type="text/javascript">var monetateT = new Date().getTime();</script>
<script type="text/javascript" src="//se.monetate.net/js/2/a-f0e60b81/p/newegg.com/entry.js"></script>
<!-- End Monetate tag. -->

	<script language="javascript" type="text/javascript">Web.Caching.SyncCookie('[{\"name\":\"NV_CONFIGURATION\",\"changeCookieValues\":[{\"key\":\"RegionCode\",\"value\":\"USA\"},{\"key\":\"CurrencyCode\",\"value\":\"USD\"},{\"key\":\"DEPA\",\"value\":\"1\"},{\"key\":\"Tid\",\"value\":\"6662\"}],\"expire\":0}]');</script>
	<script type="text/javascript">lbord=Math.random()*10000000000000000;</script>
	<script type="text/javascript">Biz.Product.video.isCookie('newegg');</script>
	<script type="text/javascript">if(top.location!=self.location){top.location.replace(self.location);}</script>
<!--[if lt IE 9]><script type="text/javascript" src="//c1.neweggimages.com/WebResource/Scripts/USA/TP_Html5/Html5.js" crossorigin="anonymous"></script><![endif]-->
</head>

<body class="NEGlobal ">
    
    <span class="noCSS">Skip to:</span>
    <a class="skiplink" href="#startContent">Content</a> 
    <a name="startContent"><span style="display: none">|</span></a>
    <span class="noCSS">|</span> 
    <a class="skiplink" href="#footerArea">Footer</a>

	<a name="top"></a>
	<div id="visionImpaired" style="position:absolute;left:0;top:-999px;"></div>
	<div id="message2OlderBrowser">
		<p>Newegg.com - A great place to buy computers, computer parts, electronics, software, accessories, and DVDs online. With great prices, fast shipping, and top-rated customer service - once you know, you Newegg.</p>
		<p>If you are reading this message, <b>Please  <a href="javascript:void(0);" onclick="window.location = window.location.href;">click this link</a> to reload this page.(Do not use your browser's "Refresh" button).</b>  Please <a href="mailto:webmaster@newegg.com">email us</a> if you're running the latest version of your browser and you still see this message.</p>
		<p><a href="https://www.newegg.com/">Newegg.com - Computer Parts, Laptops, Electronics, HDTVs, Digital Cameras and More!</a></p>
	</div>
	<noscript>
	If you see this message, your web browser doesn't support JavaScript or JavaScript is disabled. 
	Please enable JavaScript in your browser settings so Newegg.com can function correctly.
	</noscript>
	

    

    <!-- begin: header -->
    
    

<header class="header">
    <div class="header-inner">
        <div class="header-logo">
            <a href="https://www.newegg.com/" class="header-logo-img" title="Newegg.com - Computer Parts, Laptops, Electronics, HDTVs, Digital Cameras and More!">
                <img src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/logo_424x210.png" alt="Newegg.com- Computer Parts, Laptops, Electronics, HDTVs, Digital Cameras and More!"></a>
            <div class="header-logo-bg"></div>
        </div>

        <!-- begin: header tabs -->
        

<div class="header-tabs">
    <ul class="header-subsites">
        <li class="header-subsite">
            <a id="guest_feedback" onclick="javascript:newegg_inhouse_feedback && newegg_inhouse_feedback.show();" style="cursor:pointer" class="header-feedback"><ins>Feedback</ins></a>        
        </li>
        
            <li class="header-subsite">
				<a href="//www.neweggbusiness.com/?utm_medium=newegg&utm_source=newegg-home&cm_mmc=ref-newegg-_-newegg-home-_-na-_-na" target="_blank">
					<img src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/new_tab_business.png" alt="NeweggBusiness">
				</a>
            </li>
        
    </ul>
    <div class="fix"></div>
</div>

        <!-- end: header tabs -->

        <!-- begin: header top nav -->
        

<nav class="top-nav">
    <input id="hiddenOrderInfo" name="hiddenOrderInfo" type="hidden" is-update="0" value="" />
    <input type="hidden" id="switch_premier2016" value="True">
    <ul class="top-nav-tabs">
        
		
			<!--Region-->
			<li class="top-nav-tab">
				<label id="NEGlobal-CountryDropdown" for="CountryList" class="top-nav-tab-name country-change">
					
							<select id="CountryList" title="Select a Country">
						
							<optgroup label="North America">
								
										<option value="CAN" 
                                            data-countrycode="can" 
                                             
                                            data-localcurrency="USD"
                                             
                                            data-twolettercode="ca">Canada</option>
									
										<option value="MEX" 
                                            data-countrycode="mex" 
                                             
                                            data-localcurrency="MXN"
                                             
                                            data-twolettercode="mx">Mexico</option>
									
										<option value="USA" 
                                            data-countrycode="usa" 
                                            selected='selected' 
                                            data-localcurrency="USD"
                                             
                                            data-twolettercode="us">United States</option>
									
							</optgroup>
						
							<optgroup label="Oceania">
								
										<option value="AUS" 
                                            data-countrycode="aus" 
                                             
                                            data-localcurrency="AUD"
                                             
                                            data-twolettercode="au">Australia</option>
									
										<option value="NZL" 
                                            data-countrycode="nzl" 
                                             
                                            data-localcurrency="NZD"
                                             
                                            data-twolettercode="nz">New Zealand</option>
									
							</optgroup>
						
							<optgroup label="South America">
								
										<option value="CHL" 
                                            data-countrycode="chl" 
                                             
                                            data-localcurrency="USD"
                                             
                                            data-twolettercode="cl">Chile</option>
									
										<option value="COL" 
                                            data-countrycode="col" 
                                             
                                            data-localcurrency="COP"
                                             
                                            data-twolettercode="co">Colombia</option>
									
										<option value="ECU" 
                                            data-countrycode="ecu" 
                                             
                                            data-localcurrency="USD"
                                             
                                            data-twolettercode="ec">Ecuador</option>
									
							</optgroup>
						
							<optgroup label="Central America">
								
										<option value="CRI" 
                                            data-countrycode="cri" 
                                             
                                            data-localcurrency="CRC"
                                             
                                            data-twolettercode="cr">Costa Rica</option>
									
										<option value="DOM" 
                                            data-countrycode="dom" 
                                             
                                            data-localcurrency="DOP"
                                             
                                            data-twolettercode="do">Dominican Republic</option>
									
										<option value="SLV" 
                                            data-countrycode="slv" 
                                             
                                            data-localcurrency="USD"
                                             
                                            data-twolettercode="sv">El Salvador</option>
									
										<option value="HND" 
                                            data-countrycode="hnd" 
                                             
                                            data-localcurrency="HNL"
                                             
                                            data-twolettercode="hn">Honduras</option>
									
										<option value="JAM" 
                                            data-countrycode="jam" 
                                             
                                            data-localcurrency="JMD"
                                             
                                            data-twolettercode="jm">Jamaica</option>
									
										<option value="NIC" 
                                            data-countrycode="nic" 
                                             
                                            data-localcurrency="NIO"
                                             
                                            data-twolettercode="ni">Nicaragua</option>
									
										<option value="PAN" 
                                            data-countrycode="pan" 
                                             
                                            data-localcurrency="PAB"
                                             
                                            data-twolettercode="pa">Panama</option>
									
							</optgroup>
						
							<optgroup label="Asia">
								
										<option value="HKG" 
                                            data-countrycode="hkg" 
                                             
                                            data-localcurrency="HKD"
                                             
                                            data-twolettercode="hk">Hong Kong</option>
									
										<option value="IND" 
                                            data-countrycode="ind" 
                                             
                                            data-localcurrency="INR"
                                             
                                            data-twolettercode="in">India</option>
									
										<option value="IDN" 
                                            data-countrycode="idn" 
                                             
                                            data-localcurrency="IDR"
                                             
                                            data-twolettercode="id">Indonesia</option>
									
										<option value="ISR" 
                                            data-countrycode="isr" 
                                             
                                            data-localcurrency="ILS"
                                             
                                            data-twolettercode="il">Israel</option>
									
										<option value="MAC" 
                                            data-countrycode="mac" 
                                             
                                            data-localcurrency="MOP"
                                             
                                            data-twolettercode="mo">Macau</option>
									
										<option value="PHL" 
                                            data-countrycode="phl" 
                                             
                                            data-localcurrency="PHP"
                                             
                                            data-twolettercode="ph">Philippines</option>
									
										<option value="SAU" 
                                            data-countrycode="sau" 
                                             
                                            data-localcurrency="SAR"
                                             
                                            data-twolettercode="sa">Saudi Arabia</option>
									
										<option value="SGP" 
                                            data-countrycode="sgp" 
                                             
                                            data-localcurrency="SGD"
                                             
                                            data-twolettercode="sg">Singapore</option>
									
										<option value="KOR" 
                                            data-countrycode="kor" 
                                             
                                            data-localcurrency="KRW"
                                             
                                            data-twolettercode="kr">South Korea</option>
									
										<option value="THA" 
                                            data-countrycode="tha" 
                                             
                                            data-localcurrency="THB"
                                             
                                            data-twolettercode="th">Thailand</option>
									
										<option value="TUR" 
                                            data-countrycode="tur" 
                                             
                                            data-localcurrency="TRY"
                                             
                                            data-twolettercode="tr">Turkey</option>
									
										<option value="ARE" 
                                            data-countrycode="are" 
                                             
                                            data-localcurrency="AED"
                                             
                                            data-twolettercode="ae">United Arab Emirates</option>
									
							</optgroup>
						
							<optgroup label="Europe">
								
										<option value="AUT" 
                                            data-countrycode="aut" 
                                             
                                            data-localcurrency="EUR"
                                             
                                            data-twolettercode="at">Austria</option>
									
										<option value="BEL" 
                                            data-countrycode="bel" 
                                             
                                            data-localcurrency="EUR"
                                             
                                            data-twolettercode="be">Belgium</option>
									
										<option value="BGR" 
                                            data-countrycode="bgr" 
                                             
                                            data-localcurrency="BGN"
                                             
                                            data-twolettercode="bg">Bulgaria</option>
									
										<option value="DNK" 
                                            data-countrycode="dnk" 
                                             
                                            data-localcurrency="DKK"
                                             
                                            data-twolettercode="dk">Denmark</option>
									
										<option value="FIN" 
                                            data-countrycode="fin" 
                                             
                                            data-localcurrency="EUR"
                                             
                                            data-twolettercode="fi">Finland</option>
									
										<option value="FRA" 
                                            data-countrycode="fra" 
                                             
                                            data-localcurrency="EUR"
                                             
                                            data-twolettercode="fr">France</option>
									
										<option value="DEU" 
                                            data-countrycode="deu" 
                                             
                                            data-localcurrency="EUR"
                                             
                                            data-twolettercode="de">Germany</option>
									
										<option value="GRC" 
                                            data-countrycode="grc" 
                                             
                                            data-localcurrency="EUR"
                                             
                                            data-twolettercode="gr">Greece</option>
									
										<option value="HUN" 
                                            data-countrycode="hun" 
                                             
                                            data-localcurrency="HUF"
                                             
                                            data-twolettercode="hu">Hungary</option>
									
										<option value="IRL" 
                                            data-countrycode="irl" 
                                             
                                            data-localcurrency="EUR"
                                             
                                            data-twolettercode="ie">Ireland</option>
									
										<option value="ITA" 
                                            data-countrycode="ita" 
                                             
                                            data-localcurrency="EUR"
                                             
                                            data-twolettercode="it">Italy</option>
									
										<option value="LVA" 
                                            data-countrycode="lva" 
                                             
                                            data-localcurrency="EUR"
                                             
                                            data-twolettercode="lv">Latvia</option>
									
										<option value="LUX" 
                                            data-countrycode="lux" 
                                             
                                            data-localcurrency="EUR"
                                             
                                            data-twolettercode="lu">Luxembourg</option>
									
										<option value="MCO" 
                                            data-countrycode="mco" 
                                             
                                            data-localcurrency="EUR"
                                             
                                            data-twolettercode="mc">Monaco</option>
									
										<option value="NLD" 
                                            data-countrycode="nld" 
                                             
                                            data-localcurrency="EUR"
                                             
                                            data-twolettercode="nl">Netherlands</option>
									
										<option value="NOR" 
                                            data-countrycode="nor" 
                                             
                                            data-localcurrency="NOK"
                                             
                                            data-twolettercode="no">Norway</option>
									
										<option value="POL" 
                                            data-countrycode="pol" 
                                             
                                            data-localcurrency="PLN"
                                             
                                            data-twolettercode="pl">Poland</option>
									
										<option value="PRT" 
                                            data-countrycode="prt" 
                                             
                                            data-localcurrency="EUR"
                                             
                                            data-twolettercode="pt">Portugal</option>
									
										<option value="SVK" 
                                            data-countrycode="svk" 
                                             
                                            data-localcurrency="EUR"
                                             
                                            data-twolettercode="sk">Slovakia</option>
									
										<option value="SVN" 
                                            data-countrycode="svn" 
                                             
                                            data-localcurrency="EUR"
                                             
                                            data-twolettercode="si">Slovenia</option>
									
										<option value="ESP" 
                                            data-countrycode="esp" 
                                             
                                            data-localcurrency="EUR"
                                             
                                            data-twolettercode="es">Spain</option>
									
										<option value="SWE" 
                                            data-countrycode="swe" 
                                             
                                            data-localcurrency="SEK"
                                             
                                            data-twolettercode="se">Sweden</option>
									
										<option value="CHE" 
                                            data-countrycode="che" 
                                             
                                            data-localcurrency="CHF"
                                             
                                            data-twolettercode="ch">Switzerland</option>
									
										<option value="GBR" 
                                            data-countrycode="gbr" 
                                             
                                            data-localcurrency="GBP"
                                             
                                            data-twolettercode="gb">United Kingdom</option>
									
							</optgroup>
						
							</select>
						
					<span class="top-nav-tab-icon flag us"></span>
					<i class="fa fa-caret-down"></i>
				</label>
			</li>
			<script type="text/javascript">Biz.Common.TopNavigation.flagPageHeader();</script>
		
        <!--Account-->
        <li class="top-nav-tab " id='usaSite'>
            
            <script type="text/javascript">Biz.Common.TopNavigation.loginPageHeader2015();</script>
        </li>
        
            <script type="text/javascript">Biz.Common.TopNavigation.specialPricePageHeader();</script>
        
        
            <li class="top-nav-tab has-menu top-premier-menu">
                <a href="javascript:void(0);" class="top-nav-tab-name"><ins>Try</ins> <i class="icon-premier icon-premier-md-gold"></i></a>
                <div class="top-nav-menu">
                    <i class="fa fa-caret-down"></i>
                    <i class="top-nav-menu-arrow"></i>
                    <div class="top-nav-menu-inner">
                        <ul class="top-nav-menu-links">
								<li>
									<div class="top-premier-menu-title">TRY NEWEGG PREMIER FOR FREE TODAY!</div>
									<p class="top-premier-menu-note"><strong>Free 30-Day Trial</strong> when you sign up for a 12-month membership. Sign up and start enjoying:</p>
								</li>
								<li class="top-nav-menu-split">
									<div class="top-premier-menu-subtitle">Expedited Shipping</div>
									<p class="top-premier-menu-note">Free 3-Day-or-sooner expedited shipping on qualifying items.</p>
									<div class="top-premier-menu-subtitle">Share Benefits</div>
									<p class="top-premier-menu-note">Add up to four friends to your account so they can enjoy your great Newegg Premier benefits.</p>
									<div class="top-premier-menu-subtitle">Free Returns with No restocking fee</div>
									<p class="top-premier-menu-note">Free shipping on returns and waived restocking fee for qualifying items.</p>									
									<div class="top-premier-menu-subtitle">Dedicated Customer Service</div>
									<p class="top-premier-menu-note">Need quick assistance? Use our private customer service line to help answer any questions or concerns.</p>
								</li>
								<li><p class="top-premier-menu-note"><a href="//www.newegg.com/neweggpremier">Learn More</a> | <a href="https://secure.newegg.com/Premier/SignIn.aspx?code=3">Sign Up Now</a></p></li>
							</ul>
                    </div>
                </div>
            </li>
        
        <!--ShoppingCart-->
        <li class="top-nav-tab" id="miniCart">
            <script type="text/javascript">prepareMiniCartInfo(true)</script>
        </li>

        
            <li class="top-nav-tab menu-align-right has-menu" id="liWishList">
                <a href="javascript:void(0);" class="top-nav-tab-name"><i class="top-nav-tab-icon fa fa-heart"></i><ins>Wish List</ins></a>
                <div class="top-nav-menu">
                    <i class="fa fa-caret-down"></i><i class="top-nav-menu-arrow"></i>
                    <div class="top-nav-menu-inner">
                        <ul class="top-nav-menu-links">
                            <li><a href="https://secure.newegg.com/WishList/MyWishlists">My Wish Lists</a></li>
                            <li><a href="https://secure.newegg.com/WishList/FollowWishlists">Followed Wish Lists</a></li>
                            <li><a href="https://secure.newegg.com/WishList/PublicWishlists">Public Wish Lists</a></li>
                        </ul>
                    </div>
                </div>
            </li>
            <script type="text/javascript">

                var wishlistPageUrlAlias = {
                    WishListAjaxMiddlePage: "https://www.newegg.com/Common/Ajax/WishListAjaxMiddlePage.aspx",
                    MyWishListDetail: "https://secure.newegg.com/Wishlist/MyWishlistDetail", 
                    MyWishLists: "https://secure.newegg.com/WishList/MyWishlists"
                };
            </script>

            
                 <script type="text/javascript">
                     jQuery(document).ready(function () {
                         Biz.Common.TopNavigation.setWishlist(wishlistPageUrlAlias.WishListAjaxMiddlePage, wishlistPageUrlAlias.MyWishListDetail, wishlistPageUrlAlias.MyWishLists);
                     });
                 </script>
            
        

        <li class="top-nav-tab menu-align-right has-menu"><a href="javascript:void(0);" class="top-nav-tab-name"><i class="top-nav-tab-icon fa fa-question-circle"></i><ins>Customer Service</ins> </a>
            <div class="top-nav-menu">
                <i class="fa fa-caret-down"></i><i class="top-nav-menu-arrow"></i>
                <div class="top-nav-menu-inner">
                    <ul class="top-nav-menu-links">
                        <li><a id="headerTrackOrder" href="https://secure.newegg.com/Guest/OrderLogin.aspx?Source=1">Track An Order</a></li>
                        <li><a id="findInvoice" href="https://secure.newegg.com/Guest/OrderLogin.aspx?Source=4">Find Invoice</a></li>
                        <li><a id="headerReturnItem" href="https://secure.newegg.com/Guest/OrderLogin.aspx?Source=2">Return An Item</a></li>
                        <li><a id="checkReturnStatus" href="https://secure.newegg.com/Guest/OrderLogin.aspx?Source=3">Check Return Status</a></li>
                        <li><a href="//www.newegg.com/Special/Rebate.aspx?name=Rebate-Center">Find Rebates</a></li>
                        <li class="top-nav-menu-split"><a href="https://kb.newegg.com/"><i class="fa fa-info-circle"></i> Immediate Self-Help</a></li>
                        
                    </ul>
                </div>
            </div>
        </li>
    </ul>
</nav>
<script type="text/javascript">
    jQuery(document).ready(function () { Biz.Common.TopNavigation.setLink(); });
</script>

        <!-- end: header top nav -->
    </div>

    <nav class="nav-bar">
        <div class="nav-bar-inner fix">
            <div class="nav-row">
	            
                <div class="nav-col">
                    <div class="btn-group">
                        <!-- begin: site main nav -->
                        
    <nav class="btn-group-cell menu-box main-nav" id="menu_async">
        <a href="javascript:void(0);" class="btn btn-primary has-icon-right fa-caret-down main-nav-title">All Products</a>
        <div class="menu-box-body">
            <i class="menu-box-arrow"></i>
            <div id="main-nav-menu-list" class="menu-box-body-inner">
                <ul class="main-nav-categories">
                    
                </ul>
            </div>
        </div>
    </nav>








                        <!-- end: site main nav -->
                        




    <div class="btn-group-cell deals-services menu-box">
        <a href="javascript:void(0);" class="btn btn-primary has-icon-right fa-caret-down">DEALS & SERVICES</a>
        <div class="menu-box-body">
            <i class="menu-box-arrow"></i>
            <div class="menu-box-body-inner">
                <div class="nav-row">
                    
                        <div class="nav-col menu-box-split">
                            <div class="menu-box-col-260">
                                <h3 class="menu-box-title"><a href="//www.newegg.com/mobile?name=Mobile-Apps">Newegg Mobile <i class="fa fa-caret-right"></i></a></h3>
<p class="menu-box-note">Shop Exclusive Deals on our Mobile App!</p>
<h3 class="menu-box-title"><a href="//promotions.newegg.com/neemail/latest/index-landing.aspx">Email Deals <i class="fa fa-caret-right"></i></a></h3>
<p class="menu-box-note">Our latest email deals.</p>
<h3 class="menu-box-title"><a href="//www.newegg.com/DailyDeal.aspx?name=DailyDeal">Daily Deals <i class="fa fa-caret-right"></i></a></h3>
<p class="menu-box-note">New deals everyday!</p>
<h3 class="menu-box-title"><a href="//www.newegg.com/marketplace/deals">Marketplace Spotlight <i class="fa fa-caret-right"></i></a></h3>
<p class="menu-box-note">Every week, the Newegg deals team hand-picks intriguing products for you.</p>
<h3 class="menu-box-title"><a href="//www.newegg.com/Outlet/PromotionStore/ID-80">Outlet <i class="fa fa-caret-right"></i></a></h3>
<p class="menu-box-note">Open box, clearance, refurbished and recertified PCs, electronics and more.</p>
                            </div>
                        </div>
                    
                        <div class="nav-col">
                            <div class="menu-box-col-220">
                                
                                        <h3 class="menu-box-title">Sales Event</h3>
                                        <ul class="menu-box-links">
                                            
                                                    <li><a href="//www.newegg.com/promotions/nepro/18-0573/index.html">PC & Peripheral Madness</a></li>
                                                
                                                    <li><a href="//www.newegg.com/Your-Future-Is-Now/EventSaleStore/ID-1266">Your Future is Now</a></li>
                                                
                                                    <li><a href="//www.newegg.com/HomeVideo/EventSaleStore/ID-2049546">TV Store</a></li>
                                                
                                        </ul>
                                    
                                        <h3 class="menu-box-title">What's New</h3>
                                        <ul class="menu-box-links">
                                            
                                                    <li><a href="//www.newegg.com/SmartHome">Smart Home</a></li>
                                                
                                                    <li><a href="//promotions.newegg.com/intel/17-6805/index.html">Intel 8th Gen</a></li>
                                                
                                                    <li><a href="//www.newegg.com/insider">Newegg Insider</a></li>
                                                
                                                    <li><a href="//www.newegg.com/VR">VR Central</a></li>
                                                
                                        </ul>
                                    
                            </div>
                        </div>
                    
                        <div class="nav-col">
                            <div class="menu-box-col-220">
                                
                                        <h3 class="menu-box-title">More at Newegg</h3>
                                        <ul class="menu-box-links">
                                            
                                                    <li><a href="//www.newegg.com/newegg-store-credit-card">Newegg Store Credit Card</a></li>
                                                
                                                    <li><a href="//www.newegg.com/neweggpremier">Newegg Premier</a></li>
                                                
                                                    <li><a href="//www.newegg.com/neweggselect">Newegg Select</a></li>
                                                
                                                    <li><a href="//www.newegg.com/Books-Textbooks/Category/ID-551">Textbook Store</a></li>
                                                
                                                    <li><a href="//unlocked.newegg.com/">Intel Unlocked</a></li>
                                                
                                                    <li><a href="http://www.gamecrate.com/">GameCrate</a></li>
                                                
                                                    <li><a href="//promotions.newegg.com/nepro/17-6738/index.html">PC Build Kits</a></li>
                                                
                                        </ul>
                                    
                            </div>
                        </div>
                    
                        <div class="nav-col">
                            <a href="//flash.newegg.com?cm_sp=Homepage-Head2016-_-nepro%252f18-0196-_-neweggflash-_-%2f%2fpromotions.newegg.com%2fNeweggFlashBanner%2f18-0196%2f160x175_flash.jpg" class="menu-banner"><img src="//promotions.newegg.com/NeweggFlashBanner/18-0196/160x175_flash.jpg" width="160px" height="175px"></a><a href="//promotions.newegg.com/warranty/17-3252/index.html" class="menu-banner menu-banner-margin"><img src="//promotions.newegg.com/warranty/17-4182/160x175.jpg" width="160px" height="175px"></a>
                        </div>
                    
                </div>
            </div>
        </div>
    </div>




                        <!-- begin: marketplace nav -->
                        






    <nav class="btn-group-cell menu-box marketplace-nav">
        <a href="javascript:void(0);" class="btn btn-primary marketplace-nav-title has-icon-right fa-caret-down">Featured Sellers</a>
        <div class="menu-box-body marketplace-nav-body">
            <i class="menu-box-arrow"></i>
            <div class="menu-box-body-inner">
                <div class="nav-row">
                    
                        <div class="nav-col menu-box-split">
                              <div class="marketplace-nav-top fix">
												<div class="marketplace-nav-top-title">Featured Sellers</div>
												<a href="//www.newegg.com/ProductSort/TopSellerList.aspx" class="marketplace-nav-top-right">All Sellers <i class="fa fa-caret-right"></i></a>
											</div>
                                    <ul class="marketplace-nav-brands fix">
                                
												<li class="marketplace-nav-brand" style="height:75px;">
													<a href="//www.newegg.com/Adorama-Camera" >
														<img src="//images10.newegg.com/Marketing_Place/Seller_logo/Seller_A4P0_e9c6b0bb-94af-44e2-894e-dbf1de78d49b.gif" style="max-height:26px;" />
                                                    <div class="marketplace-nav-brand-rate">
                                                        <i class='rating rating-4' ></i> <strong>3697</strong>
                                                    </div>
                                            </a>
                                        </li>
                                    
												<li class="marketplace-nav-brand" style="height:75px;">
													<a href="//www.newegg.com/CRYOSTORE" >
														<img src="//images10.newegg.com/Marketing_Place/Seller_logo/Seller_A4UF_96828dde-1481-43d0-bb8f-c1340650c9b4.gif" style="max-height:26px;" />
                                                    <div class="marketplace-nav-brand-rate">
                                                        <i class='rating rating-5' ></i> <strong>3272</strong>
                                                    </div>
                                            </a>
                                        </li>
                                    
												<li class="marketplace-nav-brand" style="height:75px;">
													<a href="//www.newegg.com/DJI-Official-Store" >
														<img src="//images10.newegg.com/Marketing_Place/Seller_logo/Seller_AAWD_d4515325-3a9d-409d-9539-866d60db451d.gif" style="max-height:26px;" />
                                                    <div class="marketplace-nav-brand-rate">
                                                        <i class='rating rating-4' ></i> <strong>852</strong>
                                                    </div>
                                            </a>
                                        </li>
                                    
												<li class="marketplace-nav-brand" style="height:75px;">
													<a href="//www.newegg.com/Newedge-US" >
														<img src="//images10.newegg.com/Marketing_Place/Seller_logo/Seller_A3GY_a930ec2b-6ab1-461e-829f-8490acec2138.gif" style="max-height:26px;" />
                                                    <div class="marketplace-nav-brand-rate">
                                                        <i class='rating rating-5' ></i> <strong>952</strong>
                                                    </div>
                                            </a>
                                        </li>
                                    
												<li class="marketplace-nav-brand" style="height:75px;">
													<a href="//www.newegg.com/EK-Water-Blocks" >
														<img src="//images10.newegg.com/Marketing_Place/Seller_logo/Seller_AC8W_ad73bcc8-fce7-4158-87fc-51335b3494c9.gif" style="max-height:26px;" />
                                                    <div class="marketplace-nav-brand-rate">
                                                        <i class='rating rating-5' ></i> <strong>401</strong>
                                                    </div>
                                            </a>
                                        </li>
                                    
												<li class="marketplace-nav-brand" style="height:75px;">
													<a href="//www.newegg.com/ElectronicsExpo-com" >
														<img src="//images10.newegg.com/Marketing_Place/Seller_logo/Seller_A3JX_98434aa1-d4c7-4580-8117-a006cade2555.gif" style="max-height:26px;" />
                                                    <div class="marketplace-nav-brand-rate">
                                                        <i class='rating rating-5' ></i> <strong>662</strong>
                                                    </div>
                                            </a>
                                        </li>
                                    
												<li class="marketplace-nav-brand" style="height:75px;">
													<a href="//www.newegg.com/Music1233" >
														<img src="//images10.newegg.com/Marketing_Place/Seller_logo/Seller_AF4V_83b5605c-954b-417f-87ab-1fdf60fb4489.gif" style="max-height:26px;" />
                                                    <div class="marketplace-nav-brand-rate">
                                                        <i class='rating rating-5' ></i> <strong>13</strong>
                                                    </div>
                                            </a>
                                        </li>
                                    
												<li class="marketplace-nav-brand" style="height:75px;">
													<a href="//www.newegg.com/R1-CONCEPTS-INC" >
														<img src="//images10.newegg.com/Marketing_Place/Seller_logo/Seller_A2GG_1d2e30fd-1b39-4fe3-aa0b-6bb8f81c80e7.gif" style="max-height:26px;" />
                                                    <div class="marketplace-nav-brand-rate">
                                                        <i class='rating rating-4' ></i> <strong>95</strong>
                                                    </div>
                                            </a>
                                        </li>
                                    
												<li class="marketplace-nav-brand" style="height:75px;">
													<a href="//www.newegg.com/Sound-of-Tri-State-Inc-" >
														<img src="//images10.newegg.com/Marketing_Place/Seller_logo/Seller_A155_e2aa44ff-921a-45e9-96b9-9af8ee7c9b72.gif" style="max-height:26px;" />
                                                    <div class="marketplace-nav-brand-rate">
                                                        <i class='rating rating-5' ></i> <strong>158</strong>
                                                    </div>
                                            </a>
                                        </li>
                                    
												<li class="marketplace-nav-brand" style="height:75px;">
													<a href="//www.newegg.com/Strawberrynet" >
														<img src="//images10.newegg.com/Marketing_Place/Seller_logo/Seller_ACK0_8061046c-b3eb-4295-9d5b-eb4b4f57f1c0.gif" style="max-height:26px;" />
                                                    <div class="marketplace-nav-brand-rate">
                                                        <i class='rating rating-5' ></i> <strong>9</strong>
                                                    </div>
                                            </a>
                                        </li>
                                    
												<li class="marketplace-nav-brand" style="height:75px;">
													<a href="//www.newegg.com/Toys-R-Us-Babies-R-Us" >
														<img src="//images10.newegg.com/Marketing_Place/Seller_logo/Seller_A3G6_6a3223fb-8363-40d8-b7ba-e46ab051e980.gif" style="max-height:26px;" />
                                                    <div class="marketplace-nav-brand-rate">
                                                        <i class='rating rating-4' ></i> <strong>639</strong>
                                                    </div>
                                            </a>
                                        </li>
                                    
												<li class="marketplace-nav-brand" style="height:75px;">
													<a href="//www.newegg.com/VARIDESK" >
														<img src="//images10.newegg.com/Marketing_Place/Seller_logo/Seller_A94G_782b1bbe-5f08-44d3-b4ee-ed993bf03e49.gif" style="max-height:26px;" />
                                                    <div class="marketplace-nav-brand-rate">
                                                        <i class='rating rating-5' ></i> <strong>34</strong>
                                                    </div>
                                            </a>
                                        </li>
                                    
                            </ul>
                        </div>
                    
                        <div class="nav-col">
                            <div class="menu-box-col-260">
                                
                                        <h3 class="menu-box-title">Editor Tested</h3>
                                        <ul class="menu-box-links">
                                            
                                                    <li><a href="//www.newegg.com/insider/master-art-of-sound-headphones-tokyo-earbuds-new-york-headphones">Master Art of Sound Headphones</a></li>
                                                
                                                    <li><a href="//www.newegg.com/insider/stem-toys-robot-gift-guide-tech-kids">STEM Toy & Robot Gift Guide</a></li>
                                                
                                                    <li><a href="//www.newegg.com/insider/understanding-smart-home-communication-protocols">Building Your Smart Home Hub</a></li>
                                                
                                        </ul>
                                    
                                        <h3 class="menu-box-title">Trending Events</h3>
                                        <ul class="menu-box-links">
                                            
                                                    <li><a href="//promotions.newegg.com/marketplace/Emails/Feb-0-2018/022518/index-landing.html">Shop the Latest Refurbished Sale</a></li>
                                                
                                                    <li><a href="//www.newegg.com/Store/Brand.aspx?Brand=120625&name=The-Corn-Electronics-Store-at-Newegg?">Corn Electronics Solutions</a></li>
                                                
                                                    <li><a href="//www.newegg.com/VIVO2415/EventSaleStore/ID-2094685?">Ergonomic Desks Sale</a></li>
                                                
                                        </ul>
                                    
                                        <h3 class="menu-box-title">For Sellers</h3>
                                        <ul class="menu-box-links">
                                            
                                                    <li><a href="//www.newegg.com/sellers/">Sell on Marketplace</a></li>
                                                
                                                    <li><a href="//promotions.newegg.com/Marketplace/2017/17-1250_indiegogo/lp/index.html">Are you a startup? Join us.</a></li>
                                                
                                        </ul>
                                    
                            </div>
                        </div>
                    
                        <div class="nav-col">
                            <a href="//promotions.newegg.com/marketplace/Emails/Feb-0-2018/022518/index-landing.html" class="menu-banner"><img src="//www.newegg.com/promotions/marketplace/2018/18-0530/nav_160x360.jpg" width="160px" height="360px"></a>
                        </div>
                    
                </div>
            </div>
        </div>
    </nav>


                        <!-- end: marketplace nav -->
                    </div>
                </div>
	            
                <div class="nav-col nav-col-elastic">
                    <!-- begin: search bar -->
                    

<div id="newHeaderSearchTools" class="search-bar haFormQuickSearchTextboxWrapper">
    <script type="text/javascript">
        usingNamespace("Biz.Search")["RegionAutoFilledKeywords"] = {
            disable: 0
            };
    </script>
    <form id="haFormQuickSearch" onsubmit="return Biz.Common.QuickSearch.submitPagehHeader2011();" name="haFormQuickSearch" method="get" action="https://www.newegg.com/Product/ProductList.aspx">
        <input type="hidden" value="ENE" title="Submit" name="Submit">
        <input type="hidden" value="0" title="DEPA" name="DEPA">
        <input type="hidden" value="BESTMATCH" title="Order" name="Order">
        <input type="hidden" id="isNewHeaderTool" value="1">
        <div class="nav-row search-bar-inner">
            <div id="haQuickSearchTextbox" class="nav-col nav-col-elastic search-bar-keywords">
                <input  id="haQuickSearchBox" name="Description" title="Search Site" maxlength="268" value="video cards" type="search" autocomplete="off" onblur="Biz.Common.QuickSearch.inputFocus(false)" onwebkitspeechchange="this.value=(this.value).replace(/Keywords, Model # or Item #/,'')" onfocus="Biz.Common.QuickSearch.inputFocus(true)">
                <script type="text/javascript">Biz.Common.QuickSearch.chromeSpeechSearch(); </script>
                <div id="autofilledview" class="search-bar-auto-filled"></div>
                <iframe id="iframeKeywords" title="iframeKeywords" name="iframeKeywords" style="width: 0; height: 0; display: none;" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/blank.html">iframe for layout</iframe>
            </div>
            <!--QuickSearchDropdown-->
            <div id="haQuickSearchDropdown" class="nav-col">
                <label class="form-select search-bar-category">
                    <select id="haQuickSearchStore" title="Select a store">
                        <option value="-1" selected="selected">Search all</option><option value="100006550">Computer Systems</option><option value="100006519">Components</option><option value="100006521">Electronics</option><option value="100006616">Gaming</option><option value="100129453">Networking</option><option value="100018259">Office Solutions</option><option value="100006587">Software & Services</option><option value="100014274">Automotive & Industrial</option><option value="100006526">Home & Tools</option><option value="100010184">Health & Sports</option><option value="100161253">Apparel & Accessories</option><option value="100027683">Hobbies & Toys</option>
                    </select>
                    <span class="form-select-name">Search all</span> <i class="fa fa-caret-down"></i>
                    <input type="hidden" value="-1" title="N" name="N" id="N">
                    <input type="hidden" value="1" title="isNodeId" name="isNodeId">
                    <input type="hidden" value="" title="BRID" id="BRID">
                </label>
            </div>
            <div class="nav-col">
                <button type="button" class="btn btn-primary btn-mini search-bar-btn" onclick="javascript:Biz.Search.AutoFilledKeywordsNew.search()"  >Search</button>
            </div>
        </div>
    </form>
</div>
<script type="text/javascript">
	Biz.Search.AutoFilledKeywordsNew.init();
</script>
                    <!-- end: search bar -->
                </div>
            </div>
        </div>
    </nav>
</header>


<iframe id="commonIframe" title="commonIframe" name="commonIframe" style="width: 0; height: 0; display: none;" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/blank.html">
    iframe for layout
</iframe>

<!-- end: header -->

    <script type="text/javascript">
        (function () {
            var getUtma = function (utmaAry) {
                return utmaAry.join(".");
            };
            var getDomainHash = function (a) {
                var b = 1, c = 0, d = 0, b = 0;
                if (a) {
                    for (d = a.length - 1; 0 <= d; d--) {
                        c = a.split(/(?=[\w\W])/)[d].charCodeAt();
                        b = (b << 6 & 268435455) + c + (c << 14);
                        c = b & 266338304;
                        b = 0 != c ? b ^ c >> 21 : b;
                    }
                }
                return b;
            };
            var totalSeconds = Date.parse(new Date()) / 1000;
            var random = Math.floor(Math.random() * 1000000000);
            var getUTMAExpireTime = function () {
                return 30;
            };
            var generate = function (domain, siteID) {
                var domainHash = getDomainHash(domain);
                if (domainHash == 0) {
                    return "";
                }
                var id = random;
                var ct = totalSeconds;

                var utmaAry = new Array(7);
                utmaAry[0] = domainHash.toString();
                utmaAry[1] = siteID;
                utmaAry[2] = id.toString();
                utmaAry[3] = ct;
                utmaAry[4] = ct;
                utmaAry[5] = ct;
                utmaAry[6] = "1";

                return getUtma(utmaAry);
            };
            var refresh = function (utma, domain, siteID) {
                var utmaAry = utma.split(".");
                if (utmaAry.length == 1) {
                    return generate(domain, siteID);
                }
                if (utmaAry.length != 7) {
                    return utma;
                }

                var domainHash = getDomainHash(domain);
                if ((domainHash + "." + siteID) != (utmaAry[0] + "." + utmaAry[1])) {
                    return generate(domain, siteID);
                }

                var currentAccessTime = totalSeconds;

                var nvtcTimeStampCookie;
                var array, nvtcTimeStampRegex = new RegExp("NV_NVTCTIMESTAMP=([^;]*)(;|$)");
                if (array = document.cookie.match(nvtcTimeStampRegex)) {
                    nvtcTimeStampCookie = array[1];
                }

                if (nvtcTimeStampCookie) {
                    var nvtcTimeStamp = parseInt(nvtcTimeStampCookie);
                }
                if (!nvtcTimeStamp || (currentAccessTime - nvtcTimeStamp > getUTMAExpireTime() * 60)) {
                    utmaAry[4] = utmaAry[5];
                    utmaAry[5] = currentAccessTime.toString();
                    utmaAry[6] = parseInt(utmaAry[6]) + 1;
                    utma = getUtma(utmaAry);
                }

                return utma;
            };
            var generateAndUpdate = function () {
                try{
                    var utmaRegex = new RegExp("NVTC=([\\d\\.A-Za-z]*)");
                    var utmaMatch = utmaRegex.exec(document.cookie);
                    if (utmaMatch && utmaMatch.length > 1) {
                        var utma = utmaMatch[1];
                    }
                    var match = location.host.match(/\w+\.(\w+[\.\w+]+)/);
                    var domain;
                    if (match && match.length > 1) {
                        domain = match[1];
                    }
                    var siteID = "0001";
                    var expireDate = new Date();
                    expireDate.setFullYear(expireDate.getFullYear() + 2);

                    if (utma) {
                        var utmaAry = utma.split(".");
                        if (utmaAry.length == 7) {
                            utma = refresh(utma, domain, siteID);
                        } else {
                            utma = generate(domain, siteID);
                        }
                    } else {
                        utma = generate(domain, siteID);
                    }
                    var nvtcTimeStampExpireDate = new Date();
                    nvtcTimeStampExpireDate.setUTCDate(nvtcTimeStampExpireDate.getUTCDate() + 1);
                    document.cookie = "NVTC=" + utma + "; domain=" + domain + "; expires=" + expireDate.toGMTString() + "; path=/";
                    document.cookie = "NV_NVTCTIMESTAMP=" + totalSeconds + "; domain=" + domain + "; expires=" + nvtcTimeStampExpireDate.toGMTString() + "; path=/";
                }
                catch (ex) {
                    if (nebs) {
                        nebs.errors = nebs.errors || [];
                        nebs.errors.push(new Error('nvtcex ' + (ex.name || '') + ' ' + (ex.message || '')));
                    }
                }
            };
            
            generateAndUpdate();
        })();
    </script>


    <script type="text/javascript">
        Web.Template.RolloverMenu2015.init();
        Web.Template.PageHeaderDropDownMenu.init();
    </script>


    <!-- end: header -->

    <!-- begin: breadcrumb and top navigation -->
    
    


<div class="nav-x-body-top-bar-wrap">
    
    <div class="nav-x-body-top-bar fix">
        <ol class="breadcrumb" id="baBreadcrumbTop">
            <li>
                <a onclick="Biz.Common.SiteCatalyst.sendForOnClick({'eVar74':'Home','events':'event62'}, 'breadcrumb click');" href="https://www.newegg.com/" title="Home">Home</a>
            </li>
            
                    <li  onclick="Biz.Common.SiteCatalyst.sendForOnClick({'eVar74':'Components','events':'event62'}, 'breadcrumb click');"><a href="https://www.newegg.com/Components/Store" title="Components">Components</a></li>
                
                    <li class="is-current">Video Cards & Video Devices</li>
                
        </ol>
    </div>






    
    <div class="nav-x-body-top-bar fix">
        <script>
            jQuery(document).ready(function (e) {
                var objDelayHover = new Biz.Common.TopNavBar.objEven2016('.nav-x>.nav-x-cell.has-menu, .nav-x>.nav-x-cell.has-miniMenu');
                objDelayHover.delayHover();
            });
        </script>
        <div class="page-title" >
            <h1 class="page-title-text">Video Cards & Video Devices</h1>
        </div>
        
        <nav class="nav-x" >
            <!--begin: releated searchs rpt-->
            
            <!--end: releated searches -->
            <!--begin: releated normalNav -->
            
                    
                    
                        <div class="nav-x-cell">
                            <a href="//www.newegg.com/Gaming-Video-Cards/PromotionStore/ID-1197?cm_sp=Cat_Video-Cards_1-_-TopNav-_-Gaming-Video-Cards" title="Gaming Video Cards" class="nav-x-title">Gaming Video Cards</a>
                        </div>
                    
                
                    
                    
                        <div class="nav-x-cell">
                            <a href="//www.newegg.com/Product/ProductList.aspx?Submit=Property&amp;N=100007709%20601183313&amp;IsNodeId=1&amp;cm_sp=Cat_video-Cards_1-_-TopNav-_-VR-Ready" title="VR Ready" class="nav-x-title">VR Ready</a>
                        </div>
                    
                
                    
                    
                        <div class="nav-x-cell">
                            <a href="//www.newegg.com/Video-Cards-Video-Devices/RefurbishedStore/ID-57?name=Refurbished-Video-Cards" title="Refurbished Video Cards &amp; Devices" class="nav-x-title">Refurbished Video Cards &amp; Devices</a>
                        </div>
                    
                
            <!--end: releated normalNav -->
            <!-- begin: releated comboDealDp -->
            
            <!-- end: releated comboDealDp -->
        </nav>
    </div>



    
</div>




    <!-- end: breadcrumb and top navigation -->

    <!-- begin: page content -->
    <span id="startContent"></span>
    
    <div class="page-content">
        <section class="page-section">
            <div class="page-section-inner">
                <div class="row has-side-left">
                        <!-- begin: left side -->
                        

<div class="row-side">
    <!-- begin: left navi -->
    

<div class="left-nav">
    
            

<dl class="filter-box is-category is-active">
    
    
        <dt class="filter-box-title">Shop Category</dt>
    

    <dd class="filter-box-body">
        <ul class="filter-box-list">
            
                    <li >
                        <a href="https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48"
                             class="filter-box-label"
                            title="Desktop Graphics Cards">
                            Desktop Graphics Cards
                        </a>
                        
                    </li>
                
                    <li >
                        <a href="https://www.newegg.com/Video-Devices-TV-Tuners/SubCategory/ID-47"
                             class="filter-box-label"
                            title="Video Devices & TV Tuners">
                            Video Devices & TV Tuners
                        </a>
                        
                    </li>
                
                    <li >
                        <a href="https://www.newegg.com/Workstation-Graphics-Cards/SubCategory/ID-449"
                             class="filter-box-label"
                            title="Workstation Graphics Cards">
                            Workstation Graphics Cards
                        </a>
                        
                    </li>
                
        </ul>
    </dd>

</dl>

        
            

<dl class="filter-box is-category is-active">
    
    
        <dt class="filter-box-title">Accessories</dt>
    

    <dd class="filter-box-body">
        <ul class="filter-box-list">
            
                    <li >
                        <a href="http://www.newegg.com/Adapters-Gender-Changers/Category/ID-256?name=Other-Adapters-Gender-Changers"
                             class="filter-box-label"
                            title="Other Adapters & Gender Changers">
                            Other Adapters & Gender Changers
                        </a>
                        
                    </li>
                
                    <li >
                        <a href="https://www.newegg.com/VGA-Cooling/SubCategory/ID-576?Tid=17173"
                             class="filter-box-label"
                            title="VGA Cooling">
                            VGA Cooling
                        </a>
                        
                    </li>
                
                    <li >
                        <a href="https://www.newegg.com/Video-Card-Accessories/SubCategory/ID-321"
                             class="filter-box-label"
                            title="Video Card Accessories">
                            Video Card Accessories
                        </a>
                        
                    </li>
                
        </ul>
    </dd>

</dl>

        
</div>

    <span id="flyout-async" style="display:none">1</span>
    <script type="text/javascript">
        Web.Template.NavigationFlyout2016.init();
    </script>


    <!-- end: left navi -->
</div> 
                        <!-- end: left side -->
                    
                        <div class="row-body">
                            <div class="row-body-inner">
                                <div class="row-body-border">
                                    <!-- begin: shipping promo -->
                                    
                                    <!-- end: shipping promo -->

                                    <!-- begin: select vehicle -->
                                    
                                    <!-- end: select vehicle -->

                                    <!-- begin: leaderboard banner -->
                                    

<div class="category-banner">
    <div id="heroModule" class="swiper-container hero-banner">
        <ul class="swiper-wrapper">
            
                    <li class="swiper-slide">
                        

<a href="//www.newegg.com/videocards/EventSaleStore/ID-2041834?cm_sp=Cat_Video-Cards-Video-Devices-_-gigabyte%252f18-0146-_-%2f%2fpromotions.newegg.com%2fgigabyte%2f18-0146%2f1920x360.jpg&icid=431369"  class="category-banner-bg" style="" >
    <img src="//promotions.newegg.com/gigabyte/18-0146/1920x360.jpg" class="category-banner-img" alt="Team Up Fight On" title="GIGABYTE AMD">
</a>

                    </li>
                
                    <li class="swiper-slide">
                        

<a href="//www.newegg.com/promotions/nvidia/18-0440/index.html?cm_sp=Cat_Video-Cards-Video-Devices-_-nvidia%2f18-0440-_-https%3a%2f%2fpromotions.newegg.com%2fnvidia%2f18-0440%2f1920x360.jpg&icid=435157"  class="category-banner-bg" style="" >
    <img src="//promotions.newegg.com/nvidia/18-0440/1920x360.jpg" class="category-banner-img" alt="ULTIMATE FANTASY" title="FFXV">
</a>

                    </li>
                
                    <li class="swiper-slide">
                        

<a href="//www.newegg.com/promotions/asus/18-0020/index.html?cm_sp=Cat_Video-Cards-Video-Devices-_-nvidia%2f17-7501-_-https%3a%2f%2fpromotions.newegg.com%2fnvidia%2f17-7501%2f1920x360.jpg&icid=430938"  class="category-banner-bg" style="" >
    <img src="//promotions.newegg.com/nvidia/17-7501/1920x360.jpg" class="category-banner-img" alt="ROG STRIX GEFORCE GTX 1070 TI" title="ASUS 1070 TI">
</a>

                    </li>
                
                    <li class="swiper-slide">
                        

<a href="//www.newegg.com/videocards/EventSaleStore/ID-2041860?cm_sp=Cat_Video-Cards-Video-Devices-_-vga%252f18-0147-_-%2f%2fpromotions.newegg.com%2fvga%2f18-0147%2f1920x360.jpg&icid=432222"  class="category-banner-bg" style="" >
    <img src="//promotions.newegg.com/vga/18-0147/1920x360.jpg" class="category-banner-img" alt="Team up, fight on" title="GIGABYTE NV">
</a>

                    </li>
                
                    <li class="swiper-slide">
                        

<a href="//www.newegg.com/promotions/msi/18-0251/index.html?cm_sp=Cat_Video-Cards-Video-Devices-_-msi%2f18-0251-_-https%3a%2f%2fpromotions.newegg.com%2fmsi%2f18-0251%2f1920x360.jpg&icid=433479"  class="category-banner-bg" style="" >
    <img src="//promotions.newegg.com/msi/18-0251/1920x360.jpg" class="category-banner-img" alt="Play Hard, Stay Silent" title="MSI 10-SERIES">
</a>

                    </li>
                
                    <li class="swiper-slide">
                        

<a href="//www.newegg.com/promotions/amd/17-6965/index.html?cm_sp=Cat_Video-Cards-Video-Devices-_-amd%2f17-6965-_-https%3a%2f%2fpromotions.newegg.com%2famd%2f17-6965%2f1920x360.jpg&icid=434307"  class="category-banner-bg" style="" >
    <img src="//promotions.newegg.com/amd/17-6965/1920x360.jpg" class="category-banner-img" alt="DEFY CONVENTION" title="AMD VEGA">
</a>

                    </li>
                
                    <li class="swiper-slide">
                        

<a href="//promotions.newegg.com/amd/17-5388/index.html?cm_sp=Cat_Video-Cards-Video-Devices-_-amd%2f17-5388-_-%2f%2fpromotions.newegg.com%2famd%2f17-5388%2f1920x360.jpg&icid=427323"  class="category-banner-bg" style="" >
    <img src="//promotions.newegg.com/amd/17-5388/1920x360.jpg" class="category-banner-img" alt="The Radeon™ Vega Frontier Edition" title="VEGA Frontier">
</a>

                    </li>
                
        </ul>
        <div class="hero-banner-buttons">
            <div class="fa fa-chevron-left swiper-button-prev"></div>
            <div class="fa fa-chevron-right swiper-button-next"></div>
        </div>
    </div>
</div>

<script type="text/javascript">

    var bannerSwiper = new Swiper('#heroModule', {
        prevButton: '#heroModule .swiper-button-prev',
        nextButton: '#heroModule .swiper-button-next',
        centeredSlides: true,
        loop: true,
        autoplay: 5000,
        preventClicks: false,
        onSlideChangeStart: function () {
            this.preventClicks = true;
        },
        onSlideChangeEnd: function () {
            this.preventClicks = false;
        },
        onTouchStart: function () {
            this.preventClicks = true;
        },
        onTouchEnd: function () {
            this.preventClicks = false;
        }
    });

    jQuery('#heroModule').mouseenter(function () {
        bannerSwiper.stopAutoplay();
    }).mouseleave(function () {
        bannerSwiper.startAutoplay();
    });

    jQuery('#heroModule .swiper-button-prev, #heroModule .swiper-button-next').one('click', function () {
        jQuery('#heroModule').unbind();
    });

    /* if only one slide then */
    if (jQuery('#heroModule').find('.swiper-slide').length <= 3) {
        jQuery('#heroModule .swiper-button-prev, #heroModule .swiper-button-next').hide();
        bannerSwiper.lockSwipes();
        bannerSwiper.stopAutoplay();
    }

</script>
<!--[if lt IE 10]>
    <script>
	    var bannerSwiper = new Swiper('#heroModule',{
		    calculateHeight: true,
		    loop: true,
		    autoPlay: 5000
	    });
	    jQuery('#heroModule .swiper-button-prev').click(function(){
		    bannerSwiper.swipePrev();
	    });
	    jQuery('#heroModule .swiper-button-next').click(function(){
		    bannerSwiper.swipeNext();
	    });
	    jQuery('#heroModule').mouseenter(function(){
		    bannerSwiper.stopAutoplay();
	    }).mouseleave(function(){
		    bannerSwiper.startAutoplay();
	    });
    </script>
<![endif]-->



                                    <div class="row has-side-banner">
                                        <!-- begin: banner side-->
                                        

<div class="row-side">
	<ul class="row-side-banners">
		
				<li>
					
		

			
			<a href="//www.newegg.com/promotions/amd/17-6965/index.html?cm_sp=Cat_Video-Cards-Video-Devices-_-amd%252f17-6965-_-%2f%2fpromotions.newegg.com%2famd%2f17-6965%2f160x360.jpg&icid=434302" class="img-banners-box" target="" title="DEFY CONVENTION_0_Left" >
				<img src="//promotions.newegg.com/amd/17-6965/160x360.jpg" width="156px" alt="DEFY CONVENTION" title="DEFY CONVENTION"  >
			</a>
			
			
			

		
		








				</li>
			
				<li>
					
		

			
			<a href="//www.newegg.com/videocards/EventSaleStore/ID-2041860?cm_sp=Cat_Video-Cards-Video-Devices-_-vga%252f18-0147-_-%2f%2fpromotions.newegg.com%2fvga%2f18-0147%2f160x360.jpg&icid=432224" class="img-banners-box" target="" title="Team up, fight on_0_Left" >
				<img src="//promotions.newegg.com/vga/18-0147/160x360.jpg" width="156px" alt="Team up, fight on" title="Team up, fight on"  >
			</a>
			
			
			

		
		








				</li>
			
				<li>
					
		

			
			<a href="//www.newegg.com/videocards/PromotionStore/ID-2041598?cm_sp=Cat_Video-Cards-Video-Devices-_-vga%2f16-8455-_-http%3a%2f%2fpromotions.newegg.com%2fvga%2f16-8455%2f160x360.jpg&icid=384177" class="img-banners-box" target="" title="Video Card Clearance_0_Left" >
				<img src="//promotions.newegg.com/vga/16-8455/160x360.jpg" width="156px" alt="Video Card Clearance" title="Video Card Clearance"  >
			</a>
			
			
			

		
		








				</li>
			
				<li>
					
		

			
			<a href="//www.newegg.com/promotions/asus/18-0020/index.html?cm_sp=Cat_Video-Cards-Video-Devices-_-nvidia%2f17-7501-_-https%3a%2f%2fpromotions.newegg.com%2fnvidia%2f17-7501%2f160x360.jpg&icid=430936" class="img-banners-box" target="" title="ROG STRIX GEFORCE GTX 1070 TI_0_Left" >
				<img src="//promotions.newegg.com/nvidia/17-7501/160x360.jpg" width="156px" alt="ROG STRIX GEFORCE GTX 1070 TI" title="ROG STRIX GEFORCE GTX 1070 TI"  >
			</a>
			
			
			

		
		








				</li>
			
				<li>
					
		

			
			<a href="//www.newegg.com/videocards/EventSaleStore/ID-2041834?cm_sp=Cat_Video-Cards-Video-Devices-_-gigabyte%252f18-0146-_-%2f%2fpromotions.newegg.com%2fgigabyte%2f18-0146%2f160x360.jpg&icid=431368" class="img-banners-box" target="" title="Team Up Fight On_0_Left" >
				<img src="//promotions.newegg.com/gigabyte/18-0146/160x360.jpg" width="156px" alt="Team Up Fight On" title="Team Up Fight On"  >
			</a>
			
			
			

		
		








				</li>
			
				<li>
					
		

			
			<a href="//www.newegg.com/promotions/msi/18-0251/index.html?cm_sp=Cat_Video-Cards-Video-Devices-_-msi%2f18-0251-_-https%3a%2f%2fpromotions.newegg.com%2fmsi%2f18-0251%2f160x360.jpg&icid=433478" class="img-banners-box" target="" title="Play Hard, Stay Silent_0_Left" >
				<img src="//promotions.newegg.com/msi/18-0251/160x360.jpg" width="156px" alt="Play Hard, Stay Silent" title="Play Hard, Stay Silent"  >
			</a>
			
			
			

		
		








				</li>
			
		
			<li>
				<div class="secondary-box">
					<h3 class="secondary-box-title">Featured Brands</h3>
					<div class="secondary-box-body">
						
<div class="brands-list">
	
			<a href="https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100006662%2050001028&IsNodeId=1" class="noline">
				<img src="//images10.newegg.com/brandimage//Brand1028.gif" alt="See Deals from AMD" title="See Deals from AMD"></a>
		
			<a href="https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100006662%2050001315&IsNodeId=1" class="noline">
				<img src="//images10.newegg.com/brandimage//Brand1315.gif" alt="See Deals from ASUS" title="See Deals from ASUS"></a>
		
			<a href="https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100006662%2050001402&IsNodeId=1" class="noline">
				<img src="//images10.newegg.com/brandimage//Brand1402.gif" alt="See Deals from EVGA" title="See Deals from EVGA"></a>
		
			<a href="https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100006662%2050001314&IsNodeId=1" class="noline">
				<img src="//images10.newegg.com/brandimage//Brand1314.gif" alt="See Deals from GIGABYTE" title="See Deals from GIGABYTE"></a>
		
			<a href="https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100006662%2050001312&IsNodeId=1" class="noline">
				<img src="//images10.newegg.com/brandimage//Brand1312.gif" alt="See Deals from MSI" title="See Deals from MSI"></a>
		
			<a href="https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100006662%2050001441&IsNodeId=1" class="noline">
				<img src="//images10.newegg.com/brandimage//Brand1441.gif" alt="See Deals from NVIDIA" title="See Deals from NVIDIA"></a>
		
			<a href="https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100006662%2050001561&IsNodeId=1" class="noline">
				<img src="//images10.newegg.com/brandimage//Brand1561.gif" alt="See Deals from Sapphire Tech" title="See Deals from Sapphire Tech"></a>
		
			<a href="https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100006662%2050012150&IsNodeId=1" class="noline">
				<img src="//images10.newegg.com/brandimage//Brand12150.gif" alt="See Deals from ZOTAC" title="See Deals from ZOTAC"></a>
		
</div>

					</div>
				</div>
			</li>
		
		
			<li>
				
				<div id="hl_1_999"></div>

				
				<div id="monetate_right_bottom" class="sidebarBox"></div>
			</li>
		
		
		


		
	</ul>
</div>

                                        <!-- end: banner side-->
                                        

<div class="row-body">
    <div class="row-body-inner">
		<!-- begin: dynamic module-->
		<div class="dynamic-module-wrap">
    <div class="standard-box-top">
        <h2 class="standard-box-top-title">Shop Video Cards</h2>
    </div>
    <div class="dynamic-modules has-12-part">
        <!-- 1 -->
        <div class="dynamic-module">
            <div class="dynamic-module-img">
                <a href="//www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100007709%204814%20601201888%20601203793%20601204369%20601296707%20601301599&IsNodeId=1&cm_sp=Cat_video-Cards_1-_-Visnav-_-Gaming-Video-Cards_1" class="dynamic-module-img-inner" title="Gaming Video Cards"><img alt="Gaming Video Cards" title="Gaming Video Cards" src="//promotions.newegg.com/Visnav/Video-Cards-Video-Devices/20170116/gaming-video-cards.jpg"></a>
            </div>
            <div class="dynamic-module-info">
                <div class="dynamic-module-title">
                <a href="//www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100007709%204814%20601201888%20601203793%20601204369%20601296707%20601301599&IsNodeId=1&cm_sp=Cat_video-Cards_1-_-Visnav-_-Gaming-Video-Cards_2" title="Gaming Video Cards">Gaming Video Cards</a>
                </div>
            </div>
        </div>
        <!-- 2 -->
        <div class="dynamic-module">
            <div class="dynamic-module-img">
                <a href="//www.newegg.com/Product/ProductList.aspx?Submit=Property&N=100007709%2050001402%2050001312%2050001315%2050001561%2050001314%2050001669%2050001419%2050012150%2050001471%20600487565%20600487564%20600565503%20600582123%20600565502%20601206485%204814%20601206353%20601273503%20601273511&IsNodeId=1&cm_sp=Cat_video-Cards_2-_-Visnav-_-Performance_1" class="dynamic-module-img-inner" title="Performance Video Cards"><img alt="Performance Video Cards" title="Performance Video Cards" src="//promotions.newegg.com/Visnav/Video-Cards-Video-Devices/20170116/performance-video-cards.jpg"></a>
            </div>
            <div class="dynamic-module-info">
                <div class="dynamic-module-title">
                    <a href="//www.newegg.com/Product/ProductList.aspx?Submit=Property&N=100007709%2050001402%2050001312%2050001315%2050001561%2050001314%2050001669%2050001419%2050012150%2050001471%20600487565%20600487564%20600565503%20600582123%20600565502%20601206485%204814%20601206353%20601273503%20601273511&IsNodeId=1&cm_sp=Cat_video-Cards_2-_-Visnav-_-Performance_2" title="Performance Video Cards">Performance Video Cards</a>
                </div>
            </div>
        </div>
        <!-- 3 -->
        <div class="dynamic-module">
            <div class="dynamic-module-img">
                <a href="//www.newegg.com/Product/ProductList.aspx?Submit=Property&N=100007709%2050001402%2050001312%2050001315%2050001561%2050001314%2050001669%2050001419%2050012150%2050001471%20600528604%20600515071%20600519936%20600473873%20600473872%204814%20600083901%20601214307&IsNodeId=1&cm_sp=Cat_video-Cards_3-_-Visnav-_-Mainstream" class="dynamic-module-img-inner" title="Maintream Video Cards"><img alt="Maintream Video Cards" title="Maintream Video Cards" src="//promotions.newegg.com/Visnav/Video-Cards-Video-Devices/20170116/mainstream-video-cards.jpg"></a>
            </div>
            <div class="dynamic-module-info">
                <div class="dynamic-module-title">
                    <a href="//www.newegg.com/Product/ProductList.aspx?Submit=Property&N=100007709%2050001402%2050001312%2050001315%2050001561%2050001314%2050001669%2050001419%2050012150%2050001471%20600528604%20600515071%20600519936%20600473873%20600473872%204814%20600083901%20601214307&IsNodeId=1&cm_sp=Cat_video-Cards_3-_-Visnav-_-Mainstream" title="Maintream Video Cards">Mainstream Video Cards</a>
                </div>
            </div>
        </div>
        <!-- 4 -->
        <div class="dynamic-module">
            <div class="dynamic-module-img">
                <a href="//www.newegg.com/Product/ProductList.aspx?Submit=Property&N=100007709%2050001402%2050001312%2050001315%2050001561%2050001314%2050001669%2050001419%2050012150%2050001471%20600007541%20600335272%20600335568%20600335271%20600528884%20600007610%20600007600%20600560925%204814%20601186533&IsNodeId=1&cm_sp=Cat_video-Cards_4-_-Visnav-_-Value" class="dynamic-module-img-inner" title="Value Video Cards"><img alt="Value Video Cards" title="Value Video Cards" src="//promotions.newegg.com/Visnav/Video-Cards-Video-Devices/20170116/value-video-cards.jpg"></a>
            </div>
            <div class="dynamic-module-info">
                <div class="dynamic-module-title">
                    <a href="//www.newegg.com/Product/ProductList.aspx?Submit=Property&N=100007709%2050001402%2050001312%2050001315%2050001561%2050001314%2050001669%2050001419%2050012150%2050001471%20600007541%20600335272%20600335568%20600335271%20600528884%20600007610%20600007600%20600560925%204814%20601186533&IsNodeId=1&cm_sp=Cat_video-Cards_4-_-Visnav-_-Value" title="Value Video Cards">Value Video Cards</a>
                </div>
            </div>
        </div>
    </div>
</div>                  
<!-- end: dynamic module -->


		<!-- end: dynamic module-->

        <input type="hidden" id="isNeedIgnoreBBRParam" value="ignorebbr" />
        <!-- begin: items list -->
        
        <div class="list-wrap">
            <script type="text/javascript">
                usingNamespace("Biz.Product")["CompareConfig"] = {
                    baseQueryString: new Web.QueryStringBuilder(""),
                    PageUrlAlias: {
                        compare: "https://www.newegg.com/Product/Productcompare.aspx"
                    },
                    MasterComboId: -1,
                    SubCategoryId: "-1",
                    compareItems: [],
                    Thumbs: []
                };
            </script>
            <div class="standard-box-top">
                <h2 class="standard-box-top-title">Video Cards & Video Devices Featured Items</h2>
                
                    <a href="https://www.newegg.com/Product/ProductList.aspx?Submit=StoreIM&Depa=1&Category=38" class="link-more">
                        <span>See All</span>
                        <i class="fa fa-caret-right"></i>
                    </a>
                
            </div>
            <div class="items-view is-grid">
                
                        
                        

<div class="item-container  ">
    <!--brand info-->
    

    <!--product image-->
    <a href="https://www.newegg.com/Product/ComboBundleDetails.aspx?ItemList=Combo.3755779"  class="item-img ">
        

<img  class=" lazy-img" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/blank.gif" title="GIGABYTE Radeon RX Vega 56 DirectX 12 GV-RXVEGA56GAMING OC-8GD 8GB 2048-Bit HBM2 PCI Express 3.0 x16 CrossFireX Support ATX ..." alt="GIGABYTE Radeon RX Vega 56 DirectX 12 GV-RXVEGA56GAMING OC-8GD 8GB 2048-Bit HBM2 PCI Express 3.0 x16 CrossFireX Support ATX ..." data-src="//images10.newegg.com/NeweggImage/ProductImageCompressAll300/combo3755779.jpg" data-effect="fadeIn" />
        
    </a>
    <div class="item-info">
        <!--description info-->
        <a href="https://www.newegg.com/Product/ComboBundleDetails.aspx?ItemList=Combo.3755779" class="item-title" title="View Details">GIGABYTE Radeon RX Vega 56 DirectX 12 GV-RXVEGA56GAMING OC-8GD 8GB ...</a>
        <!--promption info-->
        
        <div class="item-action">
            <!--price-->
            

<ul class="price    ">
    <li class="price-was">
       $1,174.98
            <span class="price-was-data" style="display: none">1174.98</span>
        
    </li>
    <li class="price-map">
        
		
    </li>
    <li class="price-current">
        
            <span class="price-current-label">
			</span>$<strong>924</strong><sup>.98</sup>&nbsp;
            <span class="price-current-range">
                <abbr title="to">–</abbr>
            </span>
            
    </li>
    <li class="price-save " >
        
            <span class="price-save-endtime price-save-endtime-current"></span>
            <span class="price-save-endtime price-save-endtime-another" style="display:none;"></span>
        
        
                <span class="price-save-label">Combo save: </span>
                <span class="price-save-dollar">$250.00</span>
                <span class="price-save-percent"></span>
            
    </li>
    <li class="price-note">
        
        
    </li>
    <li class="price-ship">
        
    </li>
</ul>

            <!--egg point-->
            
            <!--button-->
            <div class="item-operate hidden-action-button ">
                <div class="item-button-area">
                    
    <button type="button"  title="Add  to cart" class="btn  btn-mini btn-primary" onClick="Biz.Product.video.conversion('cat\x3a\x7bVideo Cards \x26 Video Devices\x7d','3755779','1');Javascript:Biz.ProductList.Item.add('https://secure.newegg.com/Shopping/AddToCart.aspx?Submit=ADD&ItemList=Combo.3755779');">Add To Cart <i class="fa fa-caret-right"></i></button>



                </div>
                <!--compare-->
                
            </div>
        </div>
    </div>
    
</div>





                    
                        

<div class="item-container  ">
    <!--product image-->
    <a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814487291&ignorebbr=1" class="item-img">
        

<img  class=" lazy-img" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/blank.gif" title="EVGA&#32;GeForce&#32;GTX&#32;1050&#32;Ti&#32;SC&#32;GAMING,&#32;04G-P4-6253-KR,&#32;4GB&#32;GDDR5,&#32;DX12&#32;OSD&#32;Support&#32;&#40;PXOC&#41;" alt="EVGA&#32;GeForce&#32;GTX&#32;1050&#32;Ti&#32;SC&#32;GAMING,&#32;04G-P4-6253-KR,&#32;4GB&#32;GDDR5,&#32;DX12&#32;OSD&#32;Support&#32;&#40;PXOC&#41;" data-src="//images10.newegg.com/ProductImageCompressAll300/14-487-291-01.jpg" data-effect="fadeIn" />
    </a>
    <div class="item-info">
        <!--brand info-->
        <div class="item-branding">
            
                <a href="https://www.newegg.com/EVGA/BrandStore/ID-1402" class="item-brand">
                    

<img  class=" lazy-img" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/blank.gif" title="EVGA" alt="EVGA" data-src="//images10.newegg.com/Brandimage_70x28//Brand1402.gif" data-effect="fadeIn" />
                </a>
            
            <!--rating info-->
            
                <a title="Rating + 4" href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814487291&SortField=0&SummaryType=0&PageSize=10&SelectedRating=-1&VideoOnlyMark=False&ignorebbr=1&IsFeedbackTab=true#scrollFullInfo" class="item-rating"><i class="rating rating-4"></i><span class="item-rating-num">(94)</span></a>
            
        </div>
        <!--description info-->
        <a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814487291&ignorebbr=1"   class="item-title" title="View Details"><i class='icon-premier icon-premier-xsm'></i>EVGA GeForce GTX 1050 Ti SC GAMING, 04G-P4-6253-KR, 4GB GDDR5, DX12 OSD Support &#40;PXOC&#41;</a>
        <!--promption info-->
        <p class="item-promo"></p>
        <!--feature-->
        <ul class="item-features">
            <li><strong>Core Clock:</strong> 1354 MHz</li><li><strong>Max Resolution:</strong> 7680 x 4320</li><li><strong>DisplayPort:</strong> 1 x DisplayPort 1.4</li><li><strong>DVI:</strong> 1 x Dual-Link DVI-D</li>
            
                <li><strong>Model #: </strong>04G-P4-6253-KR</li>
            
            
                <li><strong>Item #: </strong>N82E16814487291</li>
            
            
            
        </ul>
        <div class="item-action">
            <!--price-->
            

<ul class="price   has-label-membership ">
    <li class="price-was">
       
    </li>
    <li class="price-map">
        
		
    </li>
    <li class="price-current">
        
            <span class="price-current-label">
			
                <a class="membership-info  membership-popup" name="membership" style="display: inline" data-neg-popid="MembershipPopup" href="javascript:void(0);" aria-label="Premier Price Explaination"><span class="membership-icon"></span><span style="display: none">|</span></a>
            </span>$<strong>249</strong><sup>.99</sup>&nbsp;<a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814487291&buyingoptions=New&ignorebbr=1" class="price-current-num">(8 Offers)</a>
            <span class="price-current-range">
                <abbr title="to">–</abbr>
            </span>
            
    </li>
    <li class="price-save " >
        
            <span class="price-save-endtime price-save-endtime-current"></span>
            <span class="price-save-endtime price-save-endtime-another" style="display:none;"></span>
        
        
    </li>
    <li class="price-note">
        
        
    </li>
    <li class="price-ship">
        $4.99 Shipping
    </li>
</ul>

            <!--egg point-->
            
            <!--financing-->
            
            
            <!--button-->
            <div class="item-operate hidden-action-button ">
                <div class="item-button-area">
                    
    <button type="button"  title="View Details" class="btn  btn-mini " onClick="Javascript:Biz.ProductList.Item.add('https://www.newegg.com/Product/Product.aspx?Item=N82E16814487291&ignorebbr=1');">View Details <i class="fa fa-caret-right"></i></button>



                </div>
                
                    <!--compare-->
                    <div class="item-compare-box">
                        <label class="form-checkbox">
                            <input id="CompareItem_14-487-291" autocomplete="off" neg-itemnumber="14-487-291" type="checkbox" name="CompareItem" value="CompareItem_14-487-291" aria-labelledby="checkbox_compare">
                            <span class="form-checkbox-title">Compare</span>
                        </label>
                    </div>
                    <script type="text/javascript">
                        Biz.Product.CompareConfig.compareItems.push("14-487-291");
                        var itemThumbs = new Object();
                        itemThumbs.itemNumber = "14-487-291";
                        itemThumbs.imageUrl = "//images10.newegg.com/ProductImageCompressAll35/14-487-291-01.jpg";
                        Biz.Product.CompareConfig.Thumbs.push(itemThumbs);
                    </script>
                
            </div>
        </div>
    </div>
    
</div>



                        
                    
                        

<div class="item-container  ">
    <!--product image-->
    <a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814137054&ignorebbr=1" class="item-img">
        

<img  class=" lazy-img" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/blank.gif" title="MSI&#32;GeForce&#32;GTX&#32;1050&#32;Ti&#32;DirectX&#32;12&#32;GTX&#32;1050&#32;Ti&#32;GAMING&#32;X&#32;4G&#32;4GB&#32;128-Bit&#32;GDDR5&#32;PCI&#32;Express&#32;3.0&#32;x16&#32;HDCP&#32;Ready&#32;ATX&#32;Video&#32;Card" alt="MSI&#32;GeForce&#32;GTX&#32;1050&#32;Ti&#32;DirectX&#32;12&#32;GTX&#32;1050&#32;Ti&#32;GAMING&#32;X&#32;4G&#32;4GB&#32;128-Bit&#32;GDDR5&#32;PCI&#32;Express&#32;3.0&#32;x16&#32;HDCP&#32;Ready&#32;ATX&#32;Video&#32;Card" data-src="//images10.newegg.com/ProductImageCompressAll300/14-137-054-07.jpg" data-effect="fadeIn" />
    </a>
    <div class="item-info">
        <!--brand info-->
        <div class="item-branding">
            
                <a href="https://www.newegg.com/MSI/BrandStore/ID-1312" class="item-brand">
                    

<img  class=" lazy-img" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/blank.gif" title="MSI" alt="MSI" data-src="//images10.newegg.com/Brandimage_70x28//Brand1312.gif" data-effect="fadeIn" />
                </a>
            
            <!--rating info-->
            
                <a title="Rating + 5" href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814137054&SortField=0&SummaryType=0&PageSize=10&SelectedRating=-1&VideoOnlyMark=False&ignorebbr=1&IsFeedbackTab=true#scrollFullInfo" class="item-rating"><i class="rating rating-5"></i><span class="item-rating-num">(65)</span></a>
            
        </div>
        <!--description info-->
        <a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814137054&ignorebbr=1"   class="item-title" title="View Details"><i class='icon-premier icon-premier-xsm'></i>MSI GeForce GTX 1050 Ti DirectX 12 GTX 1050 Ti GAMING X 4G Video Card</a>
        <!--promption info-->
        <p class="item-promo"></p>
        <!--feature-->
        <ul class="item-features">
            <li><strong>Core Clock:</strong> 1379 MHz (OC)
1354 MHz (Gaming)
1290 MHz (Silent)</li><li><strong>Max Resolution:</strong> 7680 x 4320</li><li><strong>DisplayPort:</strong> 1 x DisplayPort 1.4</li><li><strong>DVI:</strong> DL-DVI-D</li>
            
                <li><strong>Model #: </strong>GTX1050Ti GAMINGX 4G</li>
            
            
                <li><strong>Item #: </strong>N82E16814137054</li>
            
            
            
        </ul>
        <div class="item-action">
            <!--price-->
            

<ul class="price   has-label-membership ">
    <li class="price-was">
       
    </li>
    <li class="price-map">
        
		
    </li>
    <li class="price-current">
        
            <span class="price-current-label">
			
                <a class="membership-info  membership-popup" name="membership" style="display: inline" data-neg-popid="MembershipPopup" href="javascript:void(0);" aria-label="Premier Price Explaination"><span class="membership-icon"></span><span style="display: none">|</span></a>
            </span>$<strong>239</strong><sup>.99</sup>&nbsp;<a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814137054&buyingoptions=New&ignorebbr=1" class="price-current-num">(5 Offers)</a>
            <span class="price-current-range">
                <abbr title="to">–</abbr>
            </span>
            
    </li>
    <li class="price-save " >
        
            <span class="price-save-endtime price-save-endtime-current"></span>
            <span class="price-save-endtime price-save-endtime-another" style="display:none;"></span>
        
        
    </li>
    <li class="price-note">
        
        
    </li>
    <li class="price-ship">
        $4.99 Shipping
    </li>
</ul>

            <!--egg point-->
            
            <!--financing-->
            
            
            <!--button-->
            <div class="item-operate hidden-action-button ">
                <div class="item-button-area">
                    
    <button type="button"  title="View Details" class="btn  btn-mini " onClick="Javascript:Biz.ProductList.Item.add('https://www.newegg.com/Product/Product.aspx?Item=N82E16814137054&ignorebbr=1');">View Details <i class="fa fa-caret-right"></i></button>



                </div>
                
                    <!--compare-->
                    <div class="item-compare-box">
                        <label class="form-checkbox">
                            <input id="CompareItem_14-137-054" autocomplete="off" neg-itemnumber="14-137-054" type="checkbox" name="CompareItem" value="CompareItem_14-137-054" aria-labelledby="checkbox_compare">
                            <span class="form-checkbox-title">Compare</span>
                        </label>
                    </div>
                    <script type="text/javascript">
                        Biz.Product.CompareConfig.compareItems.push("14-137-054");
                        var itemThumbs = new Object();
                        itemThumbs.itemNumber = "14-137-054";
                        itemThumbs.imageUrl = "//images10.newegg.com/ProductImageCompressAll35/14-137-054-07.jpg";
                        Biz.Product.CompareConfig.Thumbs.push(itemThumbs);
                    </script>
                
            </div>
        </div>
    </div>
    
</div>



                        
                    
                        

<div class="item-container  ">
    <!--product image-->
    <a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814500412&ignorebbr=1" class="item-img">
        

<img  class=" lazy-img" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/blank.gif" title="ZOTAC&#32;GeForce&#32;GTX&#32;1050&#32;DirectX&#32;12&#32;ZT-P10500A-10L&#32;2GB&#32;128-Bit&#32;GDDR5&#32;PCI&#32;Express&#32;3.0&#32;HDCP&#32;Ready&#32;Video&#32;Card" alt="ZOTAC&#32;GeForce&#32;GTX&#32;1050&#32;DirectX&#32;12&#32;ZT-P10500A-10L&#32;2GB&#32;128-Bit&#32;GDDR5&#32;PCI&#32;Express&#32;3.0&#32;HDCP&#32;Ready&#32;Video&#32;Card" data-src="//images10.newegg.com/ProductImageCompressAll300/14-500-412-06.jpg" data-effect="fadeIn" />
    </a>
    <div class="item-info">
        <!--brand info-->
        <div class="item-branding">
            
                <a href="https://www.newegg.com/ZOTAC/BrandStore/ID-12150" class="item-brand">
                    

<img  class=" lazy-img" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/blank.gif" title="ZOTAC" alt="ZOTAC" data-src="//images10.newegg.com/Brandimage_70x28//Brand12150.gif" data-effect="fadeIn" />
                </a>
            
            <!--rating info-->
            
                <a title="Rating + 4" href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814500412&SortField=0&SummaryType=0&PageSize=10&SelectedRating=-1&VideoOnlyMark=False&ignorebbr=1&IsFeedbackTab=true#scrollFullInfo" class="item-rating"><i class="rating rating-4"></i><span class="item-rating-num">(38)</span></a>
            
        </div>
        <!--description info-->
        <a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814500412&ignorebbr=1"   class="item-title" title="View Details"><i class='icon-premier icon-premier-xsm'></i>ZOTAC GeForce GTX 1050 DirectX 12 ZT-P10500A-10L Video Card</a>
        <!--promption info-->
        <p class="item-promo"></p>
        <!--feature-->
        <ul class="item-features">
            <li><strong>Core Clock:</strong> 1354 MHz</li><li><strong>Max Resolution:</strong> 7680 x 4320</li><li><strong>DisplayPort:</strong> 1 x DisplayPort 1.4</li><li><strong>DVI:</strong> 1 x DL-DVI</li>
            
                <li><strong>Model #: </strong>ZT-P10500A-10L</li>
            
            
                <li><strong>Item #: </strong>N82E16814500412</li>
            
            
            
        </ul>
        <div class="item-action">
            <!--price-->
            

<ul class="price   has-label-membership ">
    <li class="price-was">
       
    </li>
    <li class="price-map">
        
		
    </li>
    <li class="price-current">
        
            <span class="price-current-label">
			
                <a class="membership-info  membership-popup" name="membership" style="display: inline" data-neg-popid="MembershipPopup" href="javascript:void(0);" aria-label="Premier Price Explaination"><span class="membership-icon"></span><span style="display: none">|</span></a>
            </span>$<strong>189</strong><sup>.99</sup>&nbsp;<a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814500412&buyingoptions=New&ignorebbr=1" class="price-current-num">(4 Offers)</a>
            <span class="price-current-range">
                <abbr title="to">–</abbr>
            </span>
            
    </li>
    <li class="price-save " >
        
            <span class="price-save-endtime price-save-endtime-current"></span>
            <span class="price-save-endtime price-save-endtime-another" style="display:none;"></span>
        
        
    </li>
    <li class="price-note">
        
        
    </li>
    <li class="price-ship">
        $4.99 Shipping
    </li>
</ul>

            <!--egg point-->
            
            <!--financing-->
            
            
            <!--button-->
            <div class="item-operate hidden-action-button ">
                <div class="item-button-area">
                    
    <button type="button"  title="View Details" class="btn  btn-mini " onClick="Javascript:Biz.ProductList.Item.add('https://www.newegg.com/Product/Product.aspx?Item=N82E16814500412&ignorebbr=1');">View Details <i class="fa fa-caret-right"></i></button>



                </div>
                
                    <!--compare-->
                    <div class="item-compare-box">
                        <label class="form-checkbox">
                            <input id="CompareItem_14-500-412" autocomplete="off" neg-itemnumber="14-500-412" type="checkbox" name="CompareItem" value="CompareItem_14-500-412" aria-labelledby="checkbox_compare">
                            <span class="form-checkbox-title">Compare</span>
                        </label>
                    </div>
                    <script type="text/javascript">
                        Biz.Product.CompareConfig.compareItems.push("14-500-412");
                        var itemThumbs = new Object();
                        itemThumbs.itemNumber = "14-500-412";
                        itemThumbs.imageUrl = "//images10.newegg.com/ProductImageCompressAll35/14-500-412-06.jpg";
                        Biz.Product.CompareConfig.Thumbs.push(itemThumbs);
                    </script>
                
            </div>
        </div>
    </div>
    
</div>



                        
                    
                        

<div class="item-container  ">
    <!--product image-->
    <a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814126169&ignorebbr=1" class="item-img">
        

<img  class=" lazy-img" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/blank.gif" title="ASUS&#32;GeForce&#32;GTX&#32;1050&#32;PH-GTX1050-2G&#32;2GB&#32;128-Bit&#32;GDDR5&#32;PCI&#32;Express&#32;3.0&#32;HDCP&#32;Ready&#32;Video&#32;Card" alt="ASUS&#32;GeForce&#32;GTX&#32;1050&#32;PH-GTX1050-2G&#32;2GB&#32;128-Bit&#32;GDDR5&#32;PCI&#32;Express&#32;3.0&#32;HDCP&#32;Ready&#32;Video&#32;Card" data-src="//images10.newegg.com/ProductImageCompressAll300/14-126-169-V01.jpg" data-effect="fadeIn" />
    </a>
    <div class="item-info">
        <!--brand info-->
        <div class="item-branding">
            
                <a href="https://www.newegg.com/ASUS/BrandStore/ID-1315" class="item-brand">
                    

<img  class=" lazy-img" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/blank.gif" title="ASUS" alt="ASUS" data-src="//images10.newegg.com/Brandimage_70x28//Brand1315.gif" data-effect="fadeIn" />
                </a>
            
            <!--rating info-->
            
                <a title="Rating + 5" href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814126169&SortField=0&SummaryType=0&PageSize=10&SelectedRating=-1&VideoOnlyMark=False&ignorebbr=1&IsFeedbackTab=true#scrollFullInfo" class="item-rating"><i class="rating rating-5"></i><span class="item-rating-num">(3)</span></a>
            
        </div>
        <!--description info-->
        <a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814126169&ignorebbr=1"   class="item-title" title="View Details"><i class='icon-premier icon-premier-xsm'></i>ASUS GeForce GTX 1050 PH-GTX1050-2G Video Card</a>
        <!--promption info-->
        <p class="item-promo"></p>
        <!--feature-->
        <ul class="item-features">
            <li><strong>Core Clock:</strong> 1354 MHz</li><li><strong>Max Resolution:</strong> 7680 x 4320</li><li><strong>DisplayPort:</strong> 1 x Native DisplayPort 1.4</li><li><strong>DVI:</strong> 1 x Native DVI-D</li>
            
                <li><strong>Model #: </strong>PH-GTX1050-2G</li>
            
            
                <li><strong>Item #: </strong>N82E16814126169</li>
            
            
            
        </ul>
        <div class="item-action">
            <!--price-->
            

<ul class="price   has-label-membership ">
    <li class="price-was">
       
    </li>
    <li class="price-map">
        
		
    </li>
    <li class="price-current">
        
            <span class="price-current-label">
			
                <a class="membership-info  membership-popup" name="membership" style="display: inline" data-neg-popid="MembershipPopup" href="javascript:void(0);" aria-label="Premier Price Explaination"><span class="membership-icon"></span><span style="display: none">|</span></a>
            </span>$<strong>164</strong><sup>.99</sup>&nbsp;<a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814126169&buyingoptions=New&ignorebbr=1" class="price-current-num">(4 Offers)</a>
            <span class="price-current-range">
                <abbr title="to">–</abbr>
            </span>
            
    </li>
    <li class="price-save " >
        
            <span class="price-save-endtime price-save-endtime-current"></span>
            <span class="price-save-endtime price-save-endtime-another" style="display:none;"></span>
        
        
    </li>
    <li class="price-note">
        
        
    </li>
    <li class="price-ship">
        $4.99 Shipping
    </li>
</ul>

            <!--egg point-->
            
            <!--financing-->
            
            
            <!--button-->
            <div class="item-operate hidden-action-button ">
                <div class="item-button-area">
                    
    <button type="button"  title="View Details" class="btn  btn-mini " onClick="Javascript:Biz.ProductList.Item.add('https://www.newegg.com/Product/Product.aspx?Item=N82E16814126169&ignorebbr=1');">View Details <i class="fa fa-caret-right"></i></button>



                </div>
                
                    <!--compare-->
                    <div class="item-compare-box">
                        <label class="form-checkbox">
                            <input id="CompareItem_14-126-169" autocomplete="off" neg-itemnumber="14-126-169" type="checkbox" name="CompareItem" value="CompareItem_14-126-169" aria-labelledby="checkbox_compare">
                            <span class="form-checkbox-title">Compare</span>
                        </label>
                    </div>
                    <script type="text/javascript">
                        Biz.Product.CompareConfig.compareItems.push("14-126-169");
                        var itemThumbs = new Object();
                        itemThumbs.itemNumber = "14-126-169";
                        itemThumbs.imageUrl = "//images10.newegg.com/ProductImageCompressAll35/14-126-169-V01.jpg";
                        Biz.Product.CompareConfig.Thumbs.push(itemThumbs);
                    </script>
                
            </div>
        </div>
    </div>
    
</div>



                        
                    
                        

<div class="item-container  ">
    <!--product image-->
    <a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814202312&ignorebbr=1" class="item-img">
        

<img  class=" lazy-img" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/blank.gif" title="SAPPHIRE&#32;NITRO&#43;&#32;Radeon&#32;RX&#32;580&#32;DirectX&#32;12&#32;100411NT&#43;4G-2L&#32;4GB&#32;256-Bit&#32;GDDR5&#32;CrossFireX&#32;Support&#32;ATX&#32;Video&#32;Card&#32;w&#47;&#32;Backplate&#32;&#40;UEFI&#41;,&#32;SAMSUNG&#32;MEMORY" alt="SAPPHIRE&#32;NITRO&#43;&#32;Radeon&#32;RX&#32;580&#32;DirectX&#32;12&#32;100411NT&#43;4G-2L&#32;4GB&#32;256-Bit&#32;GDDR5&#32;CrossFireX&#32;Support&#32;ATX&#32;Video&#32;Card&#32;w&#47;&#32;Backplate&#32;&#40;UEFI&#41;,&#32;SAMSUNG&#32;MEMORY" data-src="//images10.newegg.com/NeweggImage/ProductImageCompressAll300/14-202-312-Z01.jpg" data-effect="fadeIn" />
    </a>
    <div class="item-info">
        <!--brand info-->
        <div class="item-branding">
            
                <a href="https://www.newegg.com/Sapphire-Tech/BrandStore/ID-1561" class="item-brand">
                    

<img  class=" lazy-img" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/blank.gif" title="Sapphire Tech" alt="Sapphire Tech" data-src="//images10.newegg.com/Brandimage_70x28//Brand1561.gif" data-effect="fadeIn" />
                </a>
            
            <!--rating info-->
            
                <a title="Rating + 5" href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814202312&SortField=0&SummaryType=0&PageSize=10&SelectedRating=-1&VideoOnlyMark=False&ignorebbr=1&IsFeedbackTab=true#scrollFullInfo" class="item-rating"><i class="rating rating-5"></i><span class="item-rating-num">(1)</span></a>
            
        </div>
        <!--description info-->
        <a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814202312&ignorebbr=1"   class="item-title" title="View Details"><i class='icon-premier icon-premier-xsm'></i>SAPPHIRE NITRO&#43; Radeon RX 580 DirectX 12 100411NT&#43;4G-2L Video Card w&#47; Backplate &#40;UEFI&#41;, SAMSUNG MEMORY</a>
        <!--promption info-->
        <p class="item-promo"></p>
        <!--feature-->
        <ul class="item-features">
            <li><strong>DisplayPort:</strong> 2 x DisplayPort 1.4</li><li><strong>DVI:</strong> 1 x DVI-D</li><li><strong>HDMI:</strong> 2 x HDMI</li><li><strong>Slot Width:</strong> 2.2-slot</li>
            
                <li><strong>Model #: </strong>100411NT+4G-2L</li>
            
            
                <li><strong>Item #: </strong>N82E16814202312</li>
            
            
            
        </ul>
        <div class="item-action">
            <!--price-->
            

<ul class="price   has-label-membership ">
    <li class="price-was">
       
    </li>
    <li class="price-map">
        
		
    </li>
    <li class="price-current">
        
            <span class="price-current-label">
			
                <a class="membership-info  membership-popup" name="membership" style="display: inline" data-neg-popid="MembershipPopup" href="javascript:void(0);" aria-label="Premier Price Explaination"><span class="membership-icon"></span><span style="display: none">|</span></a>
            </span>$<strong>409</strong><sup>.99</sup>&nbsp;
            <span class="price-current-range">
                <abbr title="to">–</abbr>
            </span>
            
    </li>
    <li class="price-save " >
        
            <span class="price-save-endtime price-save-endtime-current"></span>
            <span class="price-save-endtime price-save-endtime-another" style="display:none;"></span>
        
        
    </li>
    <li class="price-note">
        
        
    </li>
    <li class="price-ship">
        $4.99 Shipping
    </li>
</ul>

            <!--egg point-->
            
            <!--financing-->
            
            
            <!--button-->
            <div class="item-operate hidden-action-button ">
                <div class="item-button-area">
                    
    <button type="button"  title="Add SAPPHIRE NITRO&#43; Radeon RX 580 DirectX 12 100411NT&#43;4G-2L Video Card w&#47; Backplate &#40;UEFI&#41;, SAMSUNG MEMORY to cart" class="btn  btn-mini btn-primary" onClick="Biz.Product.video.conversion('cat\x3a\x7bVideo Cards \x26 Video Devices\x7d','14-202-312','1');Javascript:Biz.ProductList.Item.add('https://secure.newegg.com/Shopping/AddToCart.aspx?Submit=ADD&ItemList=N82E16814202312');">Add To Cart <i class="fa fa-caret-right"></i></button>



                </div>
                
                    <!--compare-->
                    <div class="item-compare-box">
                        <label class="form-checkbox">
                            <input id="CompareItem_14-202-312" autocomplete="off" neg-itemnumber="14-202-312" type="checkbox" name="CompareItem" value="CompareItem_14-202-312" aria-labelledby="checkbox_compare">
                            <span class="form-checkbox-title">Compare</span>
                        </label>
                    </div>
                    <script type="text/javascript">
                        Biz.Product.CompareConfig.compareItems.push("14-202-312");
                        var itemThumbs = new Object();
                        itemThumbs.itemNumber = "14-202-312";
                        itemThumbs.imageUrl = "//images10.newegg.com/ProductImageCompressAll35/14-202-312-Z01.jpg";
                        Biz.Product.CompareConfig.Thumbs.push(itemThumbs);
                    </script>
                
            </div>
        </div>
    </div>
    
</div>



                        
                    
                        

<div class="item-container  ">
    <!--product image-->
    <a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814125971&ignorebbr=1" class="item-img">
        

<img  class=" lazy-img" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/blank.gif" title="GIGABYTE&#32;AORUS&#32;GeForce&#32;GTX&#32;1060&#32;6G&#32;REV&#32;2.0,&#32;GV-N1060AORUS-6GD&#32;R2" alt="GIGABYTE&#32;AORUS&#32;GeForce&#32;GTX&#32;1060&#32;6G&#32;REV&#32;2.0,&#32;GV-N1060AORUS-6GD&#32;R2" data-src="//images10.newegg.com/NeweggImage/ProductImageCompressAll300/14-125-971-Z01.jpg" data-effect="fadeIn" />
    </a>
    <div class="item-info">
        <!--brand info-->
        <div class="item-branding">
            
                <a href="https://www.newegg.com/GIGABYTE/BrandStore/ID-1314" class="item-brand">
                    

<img  class=" lazy-img" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/blank.gif" title="GIGABYTE" alt="GIGABYTE" data-src="//images10.newegg.com/Brandimage_70x28//Brand1314.gif" data-effect="fadeIn" />
                </a>
            
            <!--rating info-->
            
                <a title="Rating + 4" href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814125971&SortField=0&SummaryType=0&PageSize=10&SelectedRating=-1&VideoOnlyMark=False&ignorebbr=1&IsFeedbackTab=true#scrollFullInfo" class="item-rating"><i class="rating rating-4"></i><span class="item-rating-num">(15)</span></a>
            
        </div>
        <!--description info-->
        <a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814125971&ignorebbr=1"   class="item-title" title="View Details"><i class='icon-premier icon-premier-xsm'></i>GIGABYTE AORUS GeForce GTX 1060 6G REV 2.0, GV-N1060AORUS-6GD R2</a>
        <!--promption info-->
        <p class="item-promo"></p>
        <!--feature-->
        <ul class="item-features">
            <li><strong>Core Clock:</strong> 1632 MHz in OC mode
1607 MHz in Gaming mode</li><li><strong>Max Resolution:</strong> 7680 x 4320</li><li><strong>DisplayPort:</strong> 3 x DisplayPort 1.4</li><li><strong>DVI:</strong> 1 x Dual-link DVI-D</li>
            
                <li><strong>Model #: </strong>GV-N1060AORUS-6GD R2</li>
            
            
                <li><strong>Item #: </strong>N82E16814125971</li>
            
            
            
        </ul>
        <div class="item-action">
            <!--price-->
            

<ul class="price   has-label-membership ">
    <li class="price-was">
       
    </li>
    <li class="price-map">
        
		
    </li>
    <li class="price-current">
        
            <span class="price-current-label">
			
                <a class="membership-info  membership-popup" name="membership" style="display: inline" data-neg-popid="MembershipPopup" href="javascript:void(0);" aria-label="Premier Price Explaination"><span class="membership-icon"></span><span style="display: none">|</span></a>
            </span>$<strong>419</strong><sup>.99</sup>&nbsp;<a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814125971&buyingoptions=New&ignorebbr=1" class="price-current-num">(4 Offers)</a>
            <span class="price-current-range">
                <abbr title="to">–</abbr>
            </span>
            
    </li>
    <li class="price-save " >
        
            <span class="price-save-endtime price-save-endtime-current"></span>
            <span class="price-save-endtime price-save-endtime-another" style="display:none;"></span>
        
        
    </li>
    <li class="price-note">
        
        
    </li>
    <li class="price-ship">
        $4.99 Shipping
    </li>
</ul>

            <!--egg point-->
            
            <!--financing-->
            
            
            <!--button-->
            <div class="item-operate hidden-action-button ">
                <div class="item-button-area">
                    
    <button type="button"  title="View Details" class="btn  btn-mini " onClick="Javascript:Biz.ProductList.Item.add('https://www.newegg.com/Product/Product.aspx?Item=N82E16814125971&ignorebbr=1');">View Details <i class="fa fa-caret-right"></i></button>



                </div>
                
                    <!--compare-->
                    <div class="item-compare-box">
                        <label class="form-checkbox">
                            <input id="CompareItem_14-125-971" autocomplete="off" neg-itemnumber="14-125-971" type="checkbox" name="CompareItem" value="CompareItem_14-125-971" aria-labelledby="checkbox_compare">
                            <span class="form-checkbox-title">Compare</span>
                        </label>
                    </div>
                    <script type="text/javascript">
                        Biz.Product.CompareConfig.compareItems.push("14-125-971");
                        var itemThumbs = new Object();
                        itemThumbs.itemNumber = "14-125-971";
                        itemThumbs.imageUrl = "//images10.newegg.com/ProductImageCompressAll35/14-125-971-Z01.jpg";
                        Biz.Product.CompareConfig.Thumbs.push(itemThumbs);
                    </script>
                
            </div>
        </div>
    </div>
    
</div>



                        
                    
                        

<div class="item-container  ">
    <!--product image-->
    <a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814500411&ignorebbr=1" class="item-img">
        

<img  class=" lazy-img" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/blank.gif" title="ZOTAC&#32;GeForce&#32;GTX&#32;1050&#32;Ti&#32;DirectX&#32;12&#32;ZT-P10510A-10L&#32;4GB&#32;128-Bit&#32;GDDR5&#32;PCI&#32;Express&#32;3.0&#32;HDCP&#32;Ready&#32;Video&#32;Card" alt="ZOTAC&#32;GeForce&#32;GTX&#32;1050&#32;Ti&#32;DirectX&#32;12&#32;ZT-P10510A-10L&#32;4GB&#32;128-Bit&#32;GDDR5&#32;PCI&#32;Express&#32;3.0&#32;HDCP&#32;Ready&#32;Video&#32;Card" data-src="//images10.newegg.com/ProductImageCompressAll300/14-500-411-08.jpg" data-effect="fadeIn" />
    </a>
    <div class="item-info">
        <!--brand info-->
        <div class="item-branding">
            
                <a href="https://www.newegg.com/ZOTAC/BrandStore/ID-12150" class="item-brand">
                    

<img  class=" lazy-img" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/blank.gif" title="ZOTAC" alt="ZOTAC" data-src="//images10.newegg.com/Brandimage_70x28//Brand12150.gif" data-effect="fadeIn" />
                </a>
            
            <!--rating info-->
            
                <a title="Rating + 5" href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814500411&SortField=0&SummaryType=0&PageSize=10&SelectedRating=-1&VideoOnlyMark=False&ignorebbr=1&IsFeedbackTab=true#scrollFullInfo" class="item-rating"><i class="rating rating-5"></i><span class="item-rating-num">(50)</span></a>
            
        </div>
        <!--description info-->
        <a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814500411&ignorebbr=1"   class="item-title" title="View Details"><i class='icon-premier icon-premier-xsm'></i>ZOTAC GeForce GTX 1050 Ti DirectX 12 ZT-P10510A-10L Video Card</a>
        <!--promption info-->
        <p class="item-promo"></p>
        <!--feature-->
        <ul class="item-features">
            <li><strong>Core Clock:</strong> 1303 MHz</li><li><strong>Max Resolution:</strong> 7680 x 4320</li><li><strong>DisplayPort:</strong> 1 x DisplayPort 1.4</li><li><strong>DVI:</strong> 1 x DL-DVI-D</li>
            
                <li><strong>Model #: </strong>ZT-P10510A-10L</li>
            
            
                <li><strong>Item #: </strong>N82E16814500411</li>
            
            
            
        </ul>
        <div class="item-action">
            <!--price-->
            

<ul class="price   has-label-membership ">
    <li class="price-was">
       
    </li>
    <li class="price-map">
        
		
    </li>
    <li class="price-current">
        
            <span class="price-current-label">
			
                <a class="membership-info  membership-popup" name="membership" style="display: inline" data-neg-popid="MembershipPopup" href="javascript:void(0);" aria-label="Premier Price Explaination"><span class="membership-icon"></span><span style="display: none">|</span></a>
            </span>$<strong>234</strong><sup>.99</sup>&nbsp;<a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814500411&buyingoptions=New&ignorebbr=1" class="price-current-num">(4 Offers)</a>
            <span class="price-current-range">
                <abbr title="to">–</abbr>
            </span>
            
    </li>
    <li class="price-save " >
        
            <span class="price-save-endtime price-save-endtime-current"></span>
            <span class="price-save-endtime price-save-endtime-another" style="display:none;"></span>
        
        
    </li>
    <li class="price-note">
        
        
    </li>
    <li class="price-ship">
        $4.99 Shipping
    </li>
</ul>

            <!--egg point-->
            
            <!--financing-->
            
            
            <!--button-->
            <div class="item-operate hidden-action-button ">
                <div class="item-button-area">
                    
    <button type="button"  title="View Details" class="btn  btn-mini " onClick="Javascript:Biz.ProductList.Item.add('https://www.newegg.com/Product/Product.aspx?Item=N82E16814500411&ignorebbr=1');">View Details <i class="fa fa-caret-right"></i></button>



                </div>
                
                    <!--compare-->
                    <div class="item-compare-box">
                        <label class="form-checkbox">
                            <input id="CompareItem_14-500-411" autocomplete="off" neg-itemnumber="14-500-411" type="checkbox" name="CompareItem" value="CompareItem_14-500-411" aria-labelledby="checkbox_compare">
                            <span class="form-checkbox-title">Compare</span>
                        </label>
                    </div>
                    <script type="text/javascript">
                        Biz.Product.CompareConfig.compareItems.push("14-500-411");
                        var itemThumbs = new Object();
                        itemThumbs.itemNumber = "14-500-411";
                        itemThumbs.imageUrl = "//images10.newegg.com/ProductImageCompressAll35/14-500-411-08.jpg";
                        Biz.Product.CompareConfig.Thumbs.push(itemThumbs);
                    </script>
                
            </div>
        </div>
    </div>
    
</div>



                        
                    
                        

<div class="item-container  ">
    <!--product image-->
    <a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814126233&ignorebbr=1" class="item-img">
        

<img  class=" lazy-img" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/blank.gif" title="ASUS&#32;ROG&#32;Radeon&#32;RX&#32;Vega&#32;56&#32;STRIX-RXVEGA56-O8G-GAMING&#32;8GB&#32;2048-Bit&#32;HBM2&#32;PCI&#32;Express&#32;3.0&#32;HDCP&#32;Ready&#32;Video&#32;Card" alt="ASUS&#32;ROG&#32;Radeon&#32;RX&#32;Vega&#32;56&#32;STRIX-RXVEGA56-O8G-GAMING&#32;8GB&#32;2048-Bit&#32;HBM2&#32;PCI&#32;Express&#32;3.0&#32;HDCP&#32;Ready&#32;Video&#32;Card" data-src="//images10.newegg.com/NeweggImage/ProductImageCompressAll300/14-126-233-Z01.jpg" data-effect="fadeIn" />
    </a>
    <div class="item-info">
        <!--brand info-->
        <div class="item-branding">
            
                <a href="https://www.newegg.com/ASUS/BrandStore/ID-1315" class="item-brand">
                    

<img  class=" lazy-img" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/blank.gif" title="ASUS" alt="ASUS" data-src="//images10.newegg.com/Brandimage_70x28//Brand1315.gif" data-effect="fadeIn" />
                </a>
            
            <!--rating info-->
            
        </div>
        <!--description info-->
        <a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814126233&ignorebbr=1"   class="item-title" title="View Details"><i class='icon-premier icon-premier-xsm'></i>ASUS ROG Radeon RX Vega 56 STRIX-RXVEGA56-O8G-GAMING Video Card</a>
        <!--promption info-->
        <p class="item-promo"></p>
        <!--feature-->
        <ul class="item-features">
            <li><strong>Core Clock:</strong> 1297 MHz</li><li><strong>Max Resolution:</strong> 7680 x 4320</li><li><strong>DisplayPort:</strong> 2 x DisplayPort</li><li><strong>DVI:</strong> 1 x DVI-D</li>
            
                <li><strong>Model #: </strong>STRIX-RXVEGA56-O8G-G</li>
            
            
                <li><strong>Item #: </strong>N82E16814126233</li>
            
            
            
        </ul>
        <div class="item-action">
            <!--price-->
            

<ul class="price   has-label-membership ">
    <li class="price-was">
       
    </li>
    <li class="price-map">
        
		
    </li>
    <li class="price-current">
        
            <span class="price-current-label">
			
                <a class="membership-info  membership-popup" name="membership" style="display: inline" data-neg-popid="MembershipPopup" href="javascript:void(0);" aria-label="Premier Price Explaination"><span class="membership-icon"></span><span style="display: none">|</span></a>
            </span>$<strong>999</strong><sup>.99</sup>&nbsp;
            <span class="price-current-range">
                <abbr title="to">–</abbr>
            </span>
            
    </li>
    <li class="price-save " >
        
            <span class="price-save-endtime price-save-endtime-current"></span>
            <span class="price-save-endtime price-save-endtime-another" style="display:none;"></span>
        
        
    </li>
    <li class="price-note">
        
        
    </li>
    <li class="price-ship">
        $4.99 Shipping
    </li>
</ul>

            <!--egg point-->
            
            <!--financing-->
            
            
            <!--button-->
            <div class="item-operate hidden-action-button ">
                <div class="item-button-area">
                    
    <button type="button"  title="Add ASUS ROG Radeon RX Vega 56 STRIX-RXVEGA56-O8G-GAMING Video Card to cart" class="btn  btn-mini btn-primary" onClick="Biz.Product.video.conversion('cat\x3a\x7bVideo Cards \x26 Video Devices\x7d','14-126-233','1');Javascript:Biz.ProductList.Item.add('https://secure.newegg.com/Shopping/AddToCart.aspx?Submit=ADD&ItemList=N82E16814126233');">Add To Cart <i class="fa fa-caret-right"></i></button>



                </div>
                
                    <!--compare-->
                    <div class="item-compare-box">
                        <label class="form-checkbox">
                            <input id="CompareItem_14-126-233" autocomplete="off" neg-itemnumber="14-126-233" type="checkbox" name="CompareItem" value="CompareItem_14-126-233" aria-labelledby="checkbox_compare">
                            <span class="form-checkbox-title">Compare</span>
                        </label>
                    </div>
                    <script type="text/javascript">
                        Biz.Product.CompareConfig.compareItems.push("14-126-233");
                        var itemThumbs = new Object();
                        itemThumbs.itemNumber = "14-126-233";
                        itemThumbs.imageUrl = "//images10.newegg.com/ProductImageCompressAll35/14-126-233-Z01.jpg";
                        Biz.Product.CompareConfig.Thumbs.push(itemThumbs);
                    </script>
                
            </div>
        </div>
    </div>
    
</div>



                        
                    
                        

<div class="item-container  ">
    <!--product image-->
    <a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814137095&ignorebbr=1" class="item-img">
        

<img  class=" lazy-img" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/blank.gif" title="MSI&#32;GeForce&#32;GTX&#32;1060&#32;DirectX&#32;12&#32;GTX&#32;1060&#32;6G&#32;OCV1&#32;6GB&#32;192-Bit&#32;GDDR5&#32;PCI&#32;Express&#32;3.0&#32;x16&#32;HDCP&#32;Ready&#32;ATX&#32;Video&#32;Card" alt="MSI&#32;GeForce&#32;GTX&#32;1060&#32;DirectX&#32;12&#32;GTX&#32;1060&#32;6G&#32;OCV1&#32;6GB&#32;192-Bit&#32;GDDR5&#32;PCI&#32;Express&#32;3.0&#32;x16&#32;HDCP&#32;Ready&#32;ATX&#32;Video&#32;Card" data-src="//images10.newegg.com/NeweggImage/ProductImageCompressAll300/14-137-095-S99.jpg" data-effect="fadeIn" />
    </a>
    <div class="item-info">
        <!--brand info-->
        <div class="item-branding">
            
                <a href="https://www.newegg.com/MSI/BrandStore/ID-1312" class="item-brand">
                    

<img  class=" lazy-img" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/blank.gif" title="MSI" alt="MSI" data-src="//images10.newegg.com/Brandimage_70x28//Brand1312.gif" data-effect="fadeIn" />
                </a>
            
            <!--rating info-->
            
                <a title="Rating + 3" href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814137095&SortField=0&SummaryType=0&PageSize=10&SelectedRating=-1&VideoOnlyMark=False&ignorebbr=1&IsFeedbackTab=true#scrollFullInfo" class="item-rating"><i class="rating rating-3"></i><span class="item-rating-num">(13)</span></a>
            
        </div>
        <!--description info-->
        <a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814137095&ignorebbr=1"   class="item-title" title="View Details"><i class='icon-premier icon-premier-xsm'></i>MSI GeForce GTX 1060 DirectX 12 GTX 1060 6G OCV1 Video Card</a>
        <!--promption info-->
        <p class="item-promo"></p>
        <!--feature-->
        <ul class="item-features">
            <li><strong>Core Clock:</strong> 1544 MHz</li><li><strong>DisplayPort:</strong> 1 x DisplayPort 1.4</li><li><strong>DVI:</strong> 1 x DL-DVI-D</li><li><strong>HDMI:</strong> 1 x HDMI 2.0</li>
            
                <li><strong>Model #: </strong>GTX 1060 6GOCV1</li>
            
            
                <li><strong>Item #: </strong>N82E16814137095</li>
            
            
            
        </ul>
        <div class="item-action">
            <!--price-->
            

<ul class="price   has-label-membership ">
    <li class="price-was">
       
    </li>
    <li class="price-map">
        
		
    </li>
    <li class="price-current">
        
            <span class="price-current-label">
			
                <a class="membership-info  membership-popup" name="membership" style="display: inline" data-neg-popid="MembershipPopup" href="javascript:void(0);" aria-label="Premier Price Explaination"><span class="membership-icon"></span><span style="display: none">|</span></a>
            </span>$<strong>359</strong><sup>.99</sup>&nbsp;<a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814137095&buyingoptions=New&ignorebbr=1" class="price-current-num">(4 Offers)</a>
            <span class="price-current-range">
                <abbr title="to">–</abbr>
            </span>
            
    </li>
    <li class="price-save " >
        
            <span class="price-save-endtime price-save-endtime-current"></span>
            <span class="price-save-endtime price-save-endtime-another" style="display:none;"></span>
        
        
    </li>
    <li class="price-note">
        
        
    </li>
    <li class="price-ship">
        $4.99 Shipping
    </li>
</ul>

            <!--egg point-->
            
            <!--financing-->
            
            
            <!--button-->
            <div class="item-operate hidden-action-button ">
                <div class="item-button-area">
                    
    <button type="button"  title="View Details" class="btn  btn-mini " onClick="Javascript:Biz.ProductList.Item.add('https://www.newegg.com/Product/Product.aspx?Item=N82E16814137095&ignorebbr=1');">View Details <i class="fa fa-caret-right"></i></button>



                </div>
                
                    <!--compare-->
                    <div class="item-compare-box">
                        <label class="form-checkbox">
                            <input id="CompareItem_14-137-095" autocomplete="off" neg-itemnumber="14-137-095" type="checkbox" name="CompareItem" value="CompareItem_14-137-095" aria-labelledby="checkbox_compare">
                            <span class="form-checkbox-title">Compare</span>
                        </label>
                    </div>
                    <script type="text/javascript">
                        Biz.Product.CompareConfig.compareItems.push("14-137-095");
                        var itemThumbs = new Object();
                        itemThumbs.itemNumber = "14-137-095";
                        itemThumbs.imageUrl = "//images10.newegg.com/ProductImageCompressAll35/14-137-095-S99.jpg";
                        Biz.Product.CompareConfig.Thumbs.push(itemThumbs);
                    </script>
                
            </div>
        </div>
    </div>
    
</div>



                        
                    
                        

<div class="item-container  ">
    <!--product image-->
    <a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814487261&ignorebbr=1" class="item-img">
        

<img  class=" lazy-img" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/blank.gif" title="EVGA&#32;GeForce&#32;GTX&#32;1060&#32;SC&#32;GAMING,&#32;ACX&#32;2.0&#32;&#40;Single&#32;Fan&#41;,&#32;06G-P4-6163-KR,&#32;6GB&#32;GDDR5,&#32;DX12&#32;OSD&#32;Support&#32;&#40;PXOC&#41;,&#32;Only&#32;6.8&#32;Inches" alt="EVGA&#32;GeForce&#32;GTX&#32;1060&#32;SC&#32;GAMING,&#32;ACX&#32;2.0&#32;&#40;Single&#32;Fan&#41;,&#32;06G-P4-6163-KR,&#32;6GB&#32;GDDR5,&#32;DX12&#32;OSD&#32;Support&#32;&#40;PXOC&#41;,&#32;Only&#32;6.8&#32;Inches" data-src="//images10.newegg.com/ProductImageCompressAll300/14-487-261-S99.jpg" data-effect="fadeIn" />
    </a>
    <div class="item-info">
        <!--brand info-->
        <div class="item-branding">
            
                <a href="https://www.newegg.com/EVGA/BrandStore/ID-1402" class="item-brand">
                    

<img  class=" lazy-img" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/blank.gif" title="EVGA" alt="EVGA" data-src="//images10.newegg.com/Brandimage_70x28//Brand1402.gif" data-effect="fadeIn" />
                </a>
            
            <!--rating info-->
            
                <a title="Rating + 5" href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814487261&SortField=0&SummaryType=0&PageSize=10&SelectedRating=-1&VideoOnlyMark=False&ignorebbr=1&IsFeedbackTab=true#scrollFullInfo" class="item-rating"><i class="rating rating-5"></i><span class="item-rating-num">(205)</span></a>
            
        </div>
        <!--description info-->
        <a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814487261&ignorebbr=1"   class="item-title" title="View Details"><i class='icon-premier icon-premier-xsm'></i>EVGA GeForce GTX 1060 SC GAMING, ACX 2.0 &#40;Single Fan&#41;, 06G-P4-6163-KR, 6GB GDDR5, DX12 OSD Support &#40;PXOC&#41;, Only 6.8 Inches</a>
        <!--promption info-->
        <p class="item-promo"></p>
        <!--feature-->
        <ul class="item-features">
            <li><strong>Core Clock:</strong> 1607 MHz</li><li><strong>Max Resolution:</strong> 7680 x 4320</li><li><strong>DisplayPort:</strong> 3 x DisplayPort 1.4</li><li><strong>DVI:</strong> 1 x Dual-Link DVI-D</li>
            
                <li><strong>Model #: </strong>06G-P4-6163-KR</li>
            
            
                <li><strong>Item #: </strong>N82E16814487261</li>
            
            
            
        </ul>
        <div class="item-action">
            <!--price-->
            

<ul class="price   has-label-membership ">
    <li class="price-was">
       
    </li>
    <li class="price-map">
        
		
    </li>
    <li class="price-current">
        
            <span class="price-current-label">
			
                <a class="membership-info  membership-popup" name="membership" style="display: inline" data-neg-popid="MembershipPopup" href="javascript:void(0);" aria-label="Premier Price Explaination"><span class="membership-icon"></span><span style="display: none">|</span></a>
            </span>$<strong>359</strong><sup>.99</sup>&nbsp;<a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814487261&buyingoptions=New&ignorebbr=1" class="price-current-num">(5 Offers)</a>
            <span class="price-current-range">
                <abbr title="to">–</abbr>
            </span>
            
    </li>
    <li class="price-save " >
        
            <span class="price-save-endtime price-save-endtime-current"></span>
            <span class="price-save-endtime price-save-endtime-another" style="display:none;"></span>
        
        
    </li>
    <li class="price-note">
        
        
    </li>
    <li class="price-ship">
        $4.99 Shipping
    </li>
</ul>

            <!--egg point-->
            
            <!--financing-->
            
            
            <!--button-->
            <div class="item-operate hidden-action-button ">
                <div class="item-button-area">
                    
    <button type="button"  title="View Details" class="btn  btn-mini " onClick="Javascript:Biz.ProductList.Item.add('https://www.newegg.com/Product/Product.aspx?Item=N82E16814487261&ignorebbr=1');">View Details <i class="fa fa-caret-right"></i></button>



                </div>
                
                    <!--compare-->
                    <div class="item-compare-box">
                        <label class="form-checkbox">
                            <input id="CompareItem_14-487-261" autocomplete="off" neg-itemnumber="14-487-261" type="checkbox" name="CompareItem" value="CompareItem_14-487-261" aria-labelledby="checkbox_compare">
                            <span class="form-checkbox-title">Compare</span>
                        </label>
                    </div>
                    <script type="text/javascript">
                        Biz.Product.CompareConfig.compareItems.push("14-487-261");
                        var itemThumbs = new Object();
                        itemThumbs.itemNumber = "14-487-261";
                        itemThumbs.imageUrl = "//images10.newegg.com/ProductImageCompressAll35/14-487-261-S99.jpg";
                        Biz.Product.CompareConfig.Thumbs.push(itemThumbs);
                    </script>
                
            </div>
        </div>
    </div>
    
</div>



                        
                    
                        

<div class="item-container  ">
    <!--product image-->
    <a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814105073&ignorebbr=1" class="item-img">
        

<img  class=" lazy-img" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/blank.gif" title="AMD&#32;Radeon&#32;Vega&#32;Frontier&#32;Edition&#32;100-506061&#32;16GB&#32;2048-bit&#32;HBM2&#32;Video&#32;Cards&#32;-&#32;Workstation" alt="AMD&#32;Radeon&#32;Vega&#32;Frontier&#32;Edition&#32;100-506061&#32;16GB&#32;2048-bit&#32;HBM2&#32;Video&#32;Cards&#32;-&#32;Workstation" data-src="//images10.newegg.com/NeweggImage/ProductImageCompressAll300/14-105-073-Z01.jpg" data-effect="fadeIn" />
    </a>
    <div class="item-info">
        <!--brand info-->
        <div class="item-branding">
            
                <a href="https://www.newegg.com/AMD/BrandStore/ID-1028" class="item-brand">
                    

<img  class=" lazy-img" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/blank.gif" title="AMD" alt="AMD" data-src="//images10.newegg.com/Brandimage_70x28//Brand1028.gif" data-effect="fadeIn" />
                </a>
            
            <!--rating info-->
            
                <a title="Rating + 3" href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814105073&SortField=0&SummaryType=0&PageSize=10&SelectedRating=-1&VideoOnlyMark=False&ignorebbr=1&IsFeedbackTab=true#scrollFullInfo" class="item-rating"><i class="rating rating-3"></i><span class="item-rating-num">(58)</span></a>
            
        </div>
        <!--description info-->
        <a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814105073&ignorebbr=1"   class="item-title" title="View Details"><i class='icon-premier icon-premier-xsm'></i>AMD Radeon Vega Frontier Edition 100-506061 16GB 2048-bit HBM2 Video Cards - Workstation</a>
        <!--promption info-->
        <p class="item-promo"></p>
        <!--feature-->
        <ul class="item-features">
            <li><strong>Chipset Manufacturer:</strong> AMD</li><li><strong>Core Clock:</strong> Typical Engine Clock (MHz): 1382
Peak Engine Clock (MHz): 1600</li><li><strong>Stream Processors:</strong> 4096 Stream Processing Units</li><li><strong>Floating Point Formats:</strong> Half Precision Compute Performance: 26.2 TFLOPS
Single Precision Compute Performance: 13.1 TFLOPS
Double Precision Compute Performance: 819 GFLOPS</li>
            
                <li><strong>Model #: </strong>100-506061</li>
            
            
                <li><strong>Item #: </strong>N82E16814105073</li>
            
            
            
        </ul>
        <div class="item-action">
            <!--price-->
            

<ul class="price   has-label-membership ">
    <li class="price-was">
       
    </li>
    <li class="price-map">
        
		
    </li>
    <li class="price-current">
        
            <span class="price-current-label">
			
                <a class="membership-info  membership-popup" name="membership" style="display: inline" data-neg-popid="MembershipPopup" href="javascript:void(0);" aria-label="Premier Price Explaination"><span class="membership-icon"></span><span style="display: none">|</span></a>
            </span>$<strong>999</strong><sup>.99</sup>&nbsp;<a href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814105073&buyingoptions=New&ignorebbr=1" class="price-current-num">(2 Offers)</a>
            <span class="price-current-range">
                <abbr title="to">–</abbr>
            </span>
            
    </li>
    <li class="price-save " >
        
            <span class="price-save-endtime price-save-endtime-current"></span>
            <span class="price-save-endtime price-save-endtime-another" style="display:none;"></span>
        
        
    </li>
    <li class="price-note">
        
        
    </li>
    <li class="price-ship">
        $4.99 Shipping
    </li>
</ul>

            <!--egg point-->
            
            <!--financing-->
            
            
            <!--button-->
            <div class="item-operate hidden-action-button ">
                <div class="item-button-area">
                    
    <button type="button"  title="View Details" class="btn  btn-mini " onClick="Javascript:Biz.ProductList.Item.add('https://www.newegg.com/Product/Product.aspx?Item=N82E16814105073&ignorebbr=1');">View Details <i class="fa fa-caret-right"></i></button>



                </div>
                
                    <!--compare-->
                    <div class="item-compare-box">
                        <label class="form-checkbox">
                            <input id="CompareItem_14-105-073" autocomplete="off" neg-itemnumber="14-105-073" type="checkbox" name="CompareItem" value="CompareItem_14-105-073" aria-labelledby="checkbox_compare">
                            <span class="form-checkbox-title">Compare</span>
                        </label>
                    </div>
                    <script type="text/javascript">
                        Biz.Product.CompareConfig.compareItems.push("14-105-073");
                        var itemThumbs = new Object();
                        itemThumbs.itemNumber = "14-105-073";
                        itemThumbs.imageUrl = "//images10.newegg.com/ProductImageCompressAll35/14-105-073-Z01.jpg";
                        Biz.Product.CompareConfig.Thumbs.push(itemThumbs);
                    </script>
                
            </div>
        </div>
    </div>
    
</div>



                        
                    
            </div>
	        <span id="checkbox_compare" class="hid-text">Add To Compare</span>
            <form id="compareform" method="post" action="">
                <input type="hidden" name="CurrentUrl" id="CurrentUrl" value="" />
            </form>
            <div class="popover left popover-compare" id="compareListPopup">
                <i class="popover-arrow"></i>
                <div class="popover-title">Selected Items</div>
                <div class="popover-body">
                    <div class="item-compare-list"></div>
                    <div class="popover-btn-area">
                        <button type="button" class="btn btn-mini btn-tertiary" id="compatereset">Reset</button>
                        <button type="button" class="btn btn-mini btn-secondary" id="gocompare">Compare</button>
                    </div>
                </div>
            </div>
            <script type="text/javascript">
                NEG.domReady(function () {
                    var cfg = Biz.Product.CompareConfig;
                    var storeID = cfg.MasterComboId > 0 ? cfg.MasterComboId : cfg.SubCategoryId;
                    NEG.run(function (require) {
                        var bizCompare = require("Biz.Product.Compare");
                        var options = {
                            storeID: storeID,
                            isMasterCombo: cfg.MasterComboId > 0,
                            goCompare: function () {
                                document.getElementById('CurrentUrl') && (document.getElementById('CurrentUrl').value = window.location);
                                var compareData = this.getCompareData();
                                var compareString = this.getCompareString(compareData);
                                var items = compareData.itemList;
                                var itempers = [];

                                cfg.baseQueryString.set("CompareItemList", compareString);
                                if (Biz.Product.CompareConfig.MasterComboId > 0) {
                                    cfg.baseQueryString.set("isMasterCombo", "1");
                                }
                                var citem = "";
                                var percm = "";
                                for (var mi = 0; mi < items.length; mi++) {
                                    citem = items[mi];
                                    if (citem != null && citem.length > 0) {
                                        if (itempers[citem] != null && itempers[citem].length > 0) {
                                            percm = percm + ';' + citem + ':' + itempers[citem];
                                        }
                                    }
                                }
                                if (percm.length > 0) {
                                    percm = percm.substring(1, percm.length);
                                }
                                if (percm.length > 0) {
                                    cfg.baseQueryString.set("percm", encodeURIComponent(percm));
                                }

                                var qs = cfg.baseQueryString.toString();
                                document.forms.compareform.action = cfg.PageUrlAlias.compare + "?" + qs;
                                document.forms.compareform.submit();
                            }
                        };

                        bizCompare(options);
                    });
                });
            </script>
        </div>
        
        <!-- end: items list -->
        
            <div id="personalizationContent">
                <div class="loader">
                    <i class="fa fa-spinner fa-pulse"></i>
                    LOADING...
                </div>
                <script type="text/javascript">
                    var storeItemString = {"ItemMaintain":"4-487-291,14-137-054,14-500-412,14-126-169,14-202-312,14-125-971,14-500-411,14-126-233,14-137-095,14-487-261,14-105-073","StoreId":"38","TabStoreId":"1","StoreType":"1","Tid":"6662"};
                    var isStorePersonalizationEnable = 1;
                    var isPersonalizationEdit = 0;
                    
                    NEG.run(function (require) {
                        var viewport = require("NEG.Widget.Viewport");
                        var personalizationInit = function() {
                            var personalization = require("Biz.Store.Personalization2012")();
                            if(isStorePersonalizationEnable == 1) {
                                personalization.getData();
                            }
                        };
                        var views = [jQuery('#personalizationContent')[0]];
                        var lazyLoadViewport = viewport(views);
                        lazyLoadViewport.on("FIRSTIN", function () {
                            personalizationInit();
                        });
                        Biz.Common.CommonPop.init();
                    });

                </script>
            </div>
        
        <!-- begin: result content -->
        <!-- begin: monetate center content -->
        <div id="monetate-content-1"></div>
        <!-- end: monetate center content -->
        <!-- begin: testimonials -->
        
<div class="branding">
    <div class="branding-testimonial">
        <h3 class="branding-testimonial-title">What Customers Are Saying...</h3>
        <p class="branding-testimonial-info">
            Simply the Best &#33;&#33;&#33; 10 stars
            <br>
            <a href="https://www.newegg.com/Info/Testimonials.aspx" class="link-more">
                <span>See All</span>
                <i class="fa fa-caret-right"></i>
            </a>
        </p>
    </div>
    <!-- end: testimonials -->

    
        <div class="branding-features">
            <div class="branding-featured">
                <a href="//promotions.newegg.com/nepro/15-5021/index.html?cm_sp=newegg-store-credit-card-_-homepage-tile-_-NA-_-NA" class="branding-featured-img" title="Up to 12 Months special financing every day, every purchase." >
                    <img src="//images10.newegg.com/WebResource/Themes/2005/Nest/branding_cc.png" alt="Up to 12 Months special financing every day, every purchase." />
                </a>
                <h3>Up to 12 Months special financing every day, every purchase.</h3>
                <a href="//promotions.newegg.com/nepro/15-5021/index.html?cm_sp=newegg-store-credit-card-_-homepage-tile-_-NA-_-NA" class="link-more" title="Up to 12 Months special financing every day, every purchase." >
                    <span>Learn More</span>
                    <i class="fa fa-caret-right"></i>
                </a>
            </div>
        </div>
    
    <!-- end: three branding features -->
</div>

        <!-- end: testimonials -->

        <!--begin: SEO-->
        <div id="SEO"><div class="tab-content">
    <div class="tab-nav">
        <ul>
            <li class="is-active"><span>Overview</span></li>
            <li><span>Brand Options</span></li>
            <li><span>Specifications</span></li>
            <li><span>Accessories</span></li>
            <li><span>FAQ</span></li>
        </ul>
    </div>
    <div class="tab-pane" style="display: block;">
        <div class="article">
        <!-- START -Tab #1 Content -->
            <h3>Video & Graphics Cards</h3>
            <p>While a CPU might be considered the beating heart of your gaming pc, the graphics card can be considered the true soul of your system. It’s the piece of hardware that elevates your DIY computer from basic workstation to gaming powerhouse. You may not have a PC without a CPU, but without a graphics card, you won’t really have a gaming machine. For many people, it’s what gets them into pc building in the first place. They want the framerates and resolutions that a gaming system can offer so they can really experience true realism and immersion in their games. Current generation consoles simply can’t offer the same experience.</p>
        <!-- END -Tab #1 Content -->
        </div>
    </div>
    <div class="tab-pane" style="display: none;">
        <div class="article">
        <!-- START -Tab #2 Content -->
            <p>All video cards have the same two parts that make it capable of outputting high resolutions and framerates: the graphics processing unit (GPU) and video memory (VRAM). These come pre-installed on the PCB. Essentially, your graphics card is like a mini computer in of itself, but focused solely on processing video data. There are two main manufacturers with their own different proprietary technology: AMD and Nvidia. From there, other makers will partner with these companies to produce either factory versions of the graphics cards (such as EVGA with Nvidia), or modify the factory model with their own proprietary technology (Asus with their custom cooling).</p>
            <p>Other brands like MSI, XFX, Sapphire, Zotac, and PNY offer a variety of different cards depending on your budget and what type of gaming you want to do. The more VRAM a card has, the more likely it is able to handle multiple external displays at higher resolutions and framerates. Cards like the Nvidia GeForce GTX 980ti and the AMD Radeon R9 390 have 6-8GB of memory, which is more than enough VRAM to run even the most graphically sophisticated games at 4k resolutions without dropping below 60 frames per second. They’re also able to easily handle the specifications of an Oculus or HTC vive virtual reality headset.</p>
        <!-- END -Tab #2 Content -->
        </div>
    </div>
    <div class="tab-pane" style="display: none;">
        <div class="article">
        <!-- START -Tab #3 Content -->
            <p>A higher end card like this means more flexibility in your use-cases, however a really expensive, high-powered graphics card is not a requirement for smooth, immersive gameplay. Cards like the Nvidia GeForce GTX 970 or AMD Radeon R9 280 still have a decent amount of VRAM to handle current generation games. It just may not be able to keep up with higher resolutions as more and more graphics-intense games release. It’s up to the user to decide if they want to make the initial high-cost investment right off the bad with a more powerful card, or be satisfied with lower resolutions as their mid-range card ages.</p>
            <p>Of course, the more power a card has, the more heat it generates and the more wattage it requires. In fact, the graphics card is the most power-hungry component in your system, so you’ll have to be aware of that when building your first gaming pc or when considering a much needed upgrade. It’s generally considered a good idea to have at least 60 watts of headroom after adding up the combined wattage of your system’s components. So, if your current system uses a 650 watt power supply and you only have exactly 60 watts of headroom leftover, then you may want to also consider buying a power supply with a larger capacity before you get that R9 390 or GTX 980ti. EVGA, in addition to graphics cards, also provides PSUs. You can also check out Thermaltake, Corsair, and Seasonic.</p>
            <p>You also will probably need to upgrade your power supply if you’re adding on another video card, which is what some people do instead of just buying one powerful card. This is called SLI for Nvidia or Crossfire for AMD. Typically, it’s pretty easy to set up, as all you would need is another card of the same specifications, an SLI or Crossfire bridge (a separate component that links the two cards together, usually included in the retail box of whatever video card you’re buying), and an open PCI slot on your motherboard. This can be a more cost-effective way of upgrading your system instead of buying one brand-new, really powerful (and therefore expensive) video card.</p>
        <!-- END -Tab #3 Content -->
        </div>
    </div>
    <div class="tab-pane" style="display: none;">
        <div class="article">
        <!-- START -Tab #4 Content -->
            <p>As for the heat, there are some solutions for cooling the video card that the makers themselves have already provided out of the box. The Sapphire Radeon R9 Fury X is a self-contained liquid cooling unit that is already attached to the video card’s GPU. The all-in-one system contains the tubes, pump, and liquid pre-installed and ready to fit into your computer system, provided you have the budget and the room in your case. With a core clock of 1050 megahertz, 4 gigabytes of high-bandwidth memory (HBM), and 3 DisplayPort outputs, it can easily handle 4k gaming without turning your system into a hotbox. Liquid cooling the GPU also keeps the noise levels down, as you are lowering the amount of fans needed in your system for cooling. Some people go all out with custom liquid cooling loops, adding in custom tubing, specialized pumps and reservoirs, and metal fittings.</p>
            <p>Whether you’ve been itching to play current generation games smoothly on your PC or just getting into PC gaming, Newegg has the brands and technology to elevate your experience to the next level. Banish stuttering, low framerates, and dismal resolutions with a video card upgrade today!</p>
        <!-- END -Tab #4 Content -->
        </div>
    </div>
    <div class="tab-pane" style="display: none;">
        <div class="article">
        <!-- START -Tab #5 Content -->
            <h3>What does a video card do?</h3> 
            <p>The video card renders raw video data for visual output that is viewed on external displays such as a monitor or TV. While many CPUs have video rendering capabilities, video cards are dedicated pieces of hardware with their own graphics processing unit and video memory that fit into the PCI slot on your motherboard. It is essential to have this dedicated graphics card for playing current generation games at optimal resolutions, and is also necessary for other visually-intensive tasks like digital photo processing and 3D rendering.</p>
            <h3>What is a PCI slot?</h3> 
            <p>PCI stands for peripheral component interconnect. It is where your video card connects to the motherboard in order to talk to it and transfer information back and forth. A PCI slot can connect other hardware to the motherboard, such as a sound card or capture media card.</p>
            <h3>How is a new video card installed? </h3>
            <p>Thankfully, a video card is one of the easiest things to install in your gaming PC. The bottom of the video card has a connector that sticks out from the card’s PCB. This slots into one of the PCI slots on your motherboard. Just push down gently until it snaps into place, then secure the card’s bracket to the side of your case with the included screws.</p>
        <!-- END -Tab #5 Content -->
        </div>
    </div>
</div></div>
        <!--end: SEO-->
        <!-- end: result content -->
    </div>
    <div data-neg-title="cellphoneFreeShippping_title" style="display: none">Shipping Restrictions</div>
    <div data-neg-popid="cellphoneFreeShippping_content" style="display: none">Newegg does not process or deliver orders on weekends or holidays. Delivery will be next business day.</div>
    <div data-neg-title="cellphoneSecure_title" style="display: none">Price Available at Checkout</div>
    <div data-neg-popid="cellphoneSecure_content" style="display: none"><strong>Why can’t we show you details of this product?</strong><p>Some manufacturers place restrictions on how details of their products may be communicated.</p></div>
    <div data-neg-popid="comboSecure_content" style="display: none"><strong>How do I find out the price?</strong><ol><li>Add it to your shopping cart</li><li>Go to checkout, the price will be listed in the Order Summary</li><li>You can remove the product from your order by clicking the "Edit Shopping Cart" button</li><li>To keep it, click the "Submit Order" button</li></ol><strong>Why can’t we show you details of this product?</strong><p>Some manufacturers place restrictions on how details of their products may be communicated.</p></div>
    <div data-neg-title="comboSecure_title" style="display: none">Price Available at Checkout</div>
    <script type="text/javascript">
        jQuery(document).ready(function () {
            Biz.ProductList.Item.init();
        });
    </script>
    
        <script type="text/javascript">
            Biz.ProductList.SEO.initSEO();
        </script>
    
</div>


                                    </div>
                                </div>
                            </div>
                        </div>
                    
                </div>
            </div>
        </section>
    </div>
    <input id="product-store-version" value="2016" type="hidden" />
    
<div id="MAPpopup_Content" style="display:none;">
    <strong>How do I find out the price?</strong><ol><li>Add it to your shopping cart</li><li>Go to checkout, the price will be listed in the Order Summary</li><li>You can remove the product from your order by clicking the "Edit Shopping Cart" button</li><li>To keep it, click the "Submit Order" button</li></ol><strong>Why can’t we show you details of this product?</strong><p>Some manufacturers place restrictions on how details of their products may be communicated.</p>
</div>
<div id="CellPhoneMAPpopup_Content" style="display:none;">
    <strong>Why can’t we show you details of this product?</strong><p>Some manufacturers place restrictions on how details of their products may be communicated.</p>
</div>


    <!-- end: page content -->

    <!-- begin: footer -->
    <span id="footerArea"></span>
    
    
    <!--footer area begin-->
    <footer class="page-footer ">
        
<section class="page-section page-section-recently">
    <div class="page-section-inner">
        <div id="RecentlyItems" class="swiper-box">
            <div class="loader">
                <img src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/loading16.gif" alt="LOADING..." />
                LOADING...
            </div>
        </div>
        <script type="text/javascript">
            NEG.run(function (require) {
                var viewport = require("NEG.Widget.Viewport");
                var recentlyViewInit = function() {
                    NEG.run(function(require) {
                        var recentlyView = require("Biz.Common.RecentlyView2016")();
                        recentlyView.getData();
                    });
                };
                var views = [jQuery('#RecentlyItems')[0]];
                var lazyLoadViewport = viewport(views);
                var recentlyview = jQuery("#RecentlyItems"); 
                var topPosition = recentlyview.position().top;
                if (jQuery("#productListVersion").val() != 2016 || topPosition >= 1080) {
                	lazyLoadViewport.on("FIRSTIN", function () {
                		recentlyViewInit();
                		require('Biz.Common.Popup');
                	});
                } else {
                	recentlyViewInit();
                }
                Biz.Common.CommonPop.init();
            });
        </script>
    </div>
</section>

            <nav class="shop-region">
                
                    <div class="page-footer-inner">
                        <!--<span class="shop-region-title">Shop by Region:</span>
                        <ul class="shop-region-list">
                            
                                    <li>
                                        <strong>
                                            United States
                                        </strong>
                                    </li>
                                    <li>
                                        <a href="//www.newegg.ca">
                                            Canada
                                        </a>
                                    </li>
                                
                            <li>
                                <a href="http://www.newegg.cn" rel="nofollow">
                                    China
                                </a>
                            </li>
                            <li>
                                <a href="http://www.newegg.com.tw" rel="nofollow">Taiwan</a>
                            </li>
                        </ul> -->
                        
        <div id="google_translate_element"></div>
        <script type="text/javascript">
        function googleTranslateElementInit() {
          new google.translate.TranslateElement({pageLanguage: 'en', layout: google.translate.TranslateElement.InlineLayout.HORIZONTAL, gaTrack: true, gaId: 'UA-1147542-4'}, 'google_translate_element');
        }
        jQuery(window).load(function(){
                var a=document.createElement("script");a.type="text/javascript";a.charset="UTF-8";a.src='//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
                var b=document.getElementsByTagName("head")[0];b||(b=document.body.parentNode.appendChild(document.createElement("head")));b.appendChild(a);
        });
        </script>
      
                    </div>
                
            </nav>
        
        <nav class="footer-site-map">
            <div class="page-footer-inner nav-row">
                <ul class="nav-col first">
                    <li class="footer-site-map-title">
                        customer service
                    </li>
                    <li class="footer-site-map-item"><a href="https://kb.newegg.com/" title="Immediate Self-Help">
                        Immediate Self-Help
                    </a></li>
                    <li class="footer-site-map-item"><a id="trackOrder" rel="nofollow" title="Track an Order" href="https://secure.newegg.com/Guest/OrderLogin.aspx?Source=1">
                        Track an Order
                    </a></li>
                    <li class="footer-site-map-item"><a id="returnItem" rel="nofollow" title="Return an Item" href="https://secure.newegg.com/Guest/OrderLogin.aspx?Source=2">
                        Return an Item
                    </a></li>
                    <li class="footer-site-map-item"><a href="https://kb.newegg.com/Article/Index/12/3?id=1167" title="Return Policy"
                        rel="nofollow">
                        Return Policy
                    </a></li>
                    <li class="footer-site-map-item"><a title="Privacy & Security" href="https://kb.newegg.com/Article/Index/12/3?id=1166">
                        Privacy & Security
                    </a></li>
                    <li class="footer-site-map-item"><a title="Feedback" href="javascript:newegg_inhouse_feedback && newegg_inhouse_feedback.show();" id="footer_feedback">
                        Feedback
                    </a></li>
                    
                </ul>
                <ul class="nav-col">
                    <li class="footer-site-map-title">
                        My Account
                    </li>
                    <li class="footer-site-map-item"><a href="https://secure.newegg.com/NewMyAccount/AccountLogin.aspx" title="Login/Register">
                        Login/Register
                    </a></li>
                    <li class="footer-site-map-item"><a href="https://secure.newegg.com/NewMyAccount/Index.aspx?p=f" rel="nofollow" title="My Dashboard">
                        My Dashboard
                    </a></li>
                    <li class="footer-site-map-item"><a title="Order History" href="https://secure.newegg.com/NewMyAccount/OrderStatus.aspx"
                        rel="nofollow">
                        Order History
                    </a></li>
                    <li class="footer-site-map-item"><a rel="nofollow" title="Returns History" href="https://secure.newegg.com/RMA/Returns.aspx">
                        Returns History
                    </a></li>
                    <li class="footer-site-map-item"><a rel="nofollow" title="My Address Book" href="https://secure.newegg.com/NewMyAccount/AddressBook.aspx">
                        My Address Book
                    </a></li>
                    

                    <li class="footer-site-map-item">
                        <a rel="nofollow" title="Wish Lists" href="https://secure.newegg.com/NewMyAccount/AccountLogin.aspx?nextpage=https%3a%2f%2fwww.newegg.com%2fStore%2fCategory.aspx%3fCategory%3d38%26Tpk%3dvideo%2520cards%26recaptcha%3dpass">Wish Lists</a>
                    </li>

                    <li class="footer-site-map-item"><a id="emailNotificationFooterUrl" href="https://secure.newegg.com/Guest/EmailNotifications.aspx" title="Email Notifications" rel="nofollow">
                        Email Notifications
                    </a></li>
                    
                        <li class="footer-site-map-item"><a href="https://secure.newegg.com/NewMyAccount/NeweggSubscriptions.aspx" title="Subscriptions Orders" rel="nofollow">
                            Subscriptions Orders
                        </a></li>
                    
                    <li class="footer-site-map-item"><a rel="nofollow" title="Auto Notifications" href="https://secure.newegg.com/NewMyAccount/AutoNotifyManagement.aspx">
                        Auto Notifications
                    </a></li>
                </ul>
                <ul class="nav-col">
                    <li class="footer-site-map-title">
                        Company Information
                    </li>
                    <li class="footer-site-map-item"><a title="About Newegg" href="https://www.newegg.com/Info/AboutUs.aspx">
                        About Newegg
                    </a></li>
                    <li class="footer-site-map-item"><a title="Awards/Rankings" href="https://www.newegg.com/Info/Awards.aspx">
                        Awards/Rankings
                    </a></li>
                    <li class="footer-site-map-item"><a title="Hours and Locations" href="https://www.newegg.com/Info/OfficeHours.aspx"
                        rel="nofollow">
                        Hours and Locations
                    </a></li>
                    <li class="footer-site-map-item"><a title="Careers" href="https://www.newegg.com/Careers/TabIndex.aspx"
                        rel="nofollow">
                        Careers
                    </a></li>
                    <li class="footer-site-map-item"><a title="Newsroom" href="https://www.newegg.com/Info/Newsroom.aspx">
                        Newsroom
                    </a></li>
                    
                        <li class="footer-site-map-item"><a title="Newegg Insider" href="https://www.newegg.com/insider/"
                            target="_blank">
                            Newegg Insider
                        </a></li>
                    
                        <li class="footer-site-map-item"><a title="Calif. Transparency in Supply Chains Act " href="https://kb.newegg.com/Article/Index/12/3?id=1331">
                            Calif. Transparency <br/>in Supply Chains Act 
                        </a></li>
                    
                </ul>
                <ul class="nav-col">
                    <li class="footer-site-map-title">
                        Tools & Resources
                    </li>
                    <li class="footer-site-map-item"><a title="Sell on Newegg Marketplace" href="//www.newegg.com/sellers/" rel="nofollow">
                        Sell on Newegg Marketplace
                    </a></li>
                    
                        <li class="footer-site-map-item"><a title="Shipped by Newegg" href="https://www.newegg.com/sellers/index.php/shipped-by-newegg/" rel="nofollow">
                            Shipped by Newegg
                        </a></li>
                    
                    <li class="footer-site-map-item"><a title="Become an Affiliate" href="https://www.newegg.com/Info/Affiliates.aspx">
                        Become an Affiliate
                    </a></li>
                    <li class="footer-site-map-item"><a title="Become a Newegg Vendor" href="//promotions.newegg.com/nepro/12-0435/index.html">
                        Become a Newegg Vendor
                    </a></li>
                    <li class="footer-site-map-item"><a title="Site Map" href="https://www.newegg.com/Info/SiteMap.aspx">
                        Site Map
                    </a></li>
                    
                        <li class="footer-site-map-item"><a href="https://www.newegg.com/ProductSort/BrandList.aspx?Depa=0" title="Shop by Brand" 
                            rel="nofollow">
                            Shop by Brand
                        </a></li>
                    
                    <li class="footer-site-map-item"><a title="Product Review" href="https://www.newegg.com/Feedback/Reviews.aspx"
                        rel="nofollow">
                        Product Review
                    </a></li>
                    <li class="footer-site-map-item"><a title="Video Center" href="//www.newegg.tv/"
                        rel="nofollow">
                        Video Center
                    </a></li>
                    <li class="footer-site-map-item"><a title="Rebates" href="https://www.newegg.com/Special/Rebate.aspx?name=Rebate-Center">
                        Rebates
                    </a></li>
                    
                        <li class="footer-site-map-item"><a href="//www.newegg.com/promotions/warranty/18-0191/index.html" title="Trade-In Your Items" rel="nofollow">
                            Trade-In Your Items
                        </a></li>
                    
                    <li class="footer-site-map-item"><a title="Mobile Apps" href="http://www.newegg.com/mobile?name=Mobile-Apps"
                        rel="nofollow">
                        Mobile Apps
                    </a></li>
                </ul>
            </div>
        </nav>
        
            <nav class="shop-region">
                <div class="page-footer-inner">
                    <!--<span class="shop-region-title">
                        Affiliated Sites:
                    </span>-->
                    <ul class="shop-region-list">
                            <li>
                                <a title="Newegg Global(new window)"
                                    target="_blank" rel="nofollow" href="https://promotions.newegg.com/international/global/index.html">
                                    Newegg Global
                                    <br>
                                    <span class="shop-region-list-note">
                                        International Shopping
                                    </span>
                                </a>
                            </li>
                        
                            <li>
                                <a title="Newegg Retail Site(new window)"
                                    target="_blank" rel="nofollow" href="//www.neweggbusiness.com/">
                                     NeweggBusiness
                                    <br>
                                    <span class="shop-region-list-note">
                                        For Business Needs
                                    </span>
                                </a>
                            </li>
                        
                            <li>
                                <a title="Newegg Community(new window)" target="_blank"
                                    rel="nofollow" href="https://community.newegg.com/">
                                    Newegg Community
                                    <br>
                                    <span class="shop-region-list-note">
                                        Newegg Community
                                    </span>

                                </a>
                            </li>
                        
                            <li>
                                <a title="Newegg GameCrate(new window)" target="_blank"
                                    rel="nofollow" href="http://www.gamecrate.com/">
                                    Newegg GameCrate
                                    <br>
                                    <span class="shop-region-list-note">
                                        Gaming and Hardware News
                                    </span>
                                </a>
                            </li>
                        
                    </ul>
                    <ul class="social-follow-list">
                        
                                <li class="social-follow-item">
                                    <a class="fa fa-facebook social-follow-item-icon" aria-label="Facebook" target="_blank" href="http://www.facebook.com/Newegg"><span style="display: none">Facebook</span></a>
                                </li>
                                <li class="social-follow-item">
                                    <a class="fa fa-twitter social-follow-item-icon" aria-label="Twitter" target="_blank" href="http://twitter.com/Newegg"><span style="display: none">Twitter</span></a>
                                </li>
                                <li class="social-follow-item">
                                    <a class="fa fa-instagram social-follow-item-icon" aria-label="Instagram" target="_blank" href="http://instagram.com/newegg/"><span style="display: none">Instagram</span></a>
                                </li>
                                <li class="social-follow-item">
                                    <a class="fa fa-google-plus social-follow-item-icon" aria-label="Google" target="_blank" href="https://plus.google.com/+Newegg"><span style="display: none">Google</span></a>
                                </li>
                                <li class="social-follow-item">
                                    <a class="fa fa-pinterest social-follow-item-icon" aria-label="Pinterest" target="_blank" href="http://pinterest.com/newegg/"><span style="display: none">Pinterest</span></a>
                                </li>
                                <li class="social-follow-item">
                                    <a class="fa fa-youtube-play social-follow-item-icon" aria-label="YouTube" target="_blank" href="http://www.youtube.com/neweggtv"><span style="display: none">YouTube</span></a>
                                </li>
                                
                                    <li class="social-follow-item">
                                        <a class="fa fa-rss social-follow-item-icon" aria-label="Rss" target="_blank" href="https://www.newegg.com/RSS/Index.aspx"><span style="display: none">Rss</span></a>
                                    </li>
                                
                    </ul>
                </div>
            </nav>
        
        <div id="footerAwards" class="footer-awards">
            <script type="text/javascript">
                usingNamespace("Biz.Footer")["Config"] = {
                    veriSignUrl: "https://trustsealinfo.websecurity.norton.com/splash?form_file=fdf/splash.fdf&dn=SECURE.NEWEGG.COM&lang=en"
                };
            </script>

            
                    <a href="javascript:Biz.Common.VeriSign.open();" class="noline">
                        <img src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/awards_04.gif" style="border: 0;" alt="VeriSign">
                    </a>
                
                    <a class="noline" href="//www.resellerratings.com/store/Newegg">
                        <img src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/resellerRatings_105x75.gif" alt="Reseller Ratings" style="border: 0pt none;" />
                    </a>
                
                    <a class="noline" title="Click for the BBB Business Review of this Computers - Supplies & Parts in Whittier CA" href="https://www.bbb.org/losangelessiliconvalley/business-reviews/computers-supplies-and-parts/newegg-in-whittier-ca-13146135">
                        <img alt="Click for the BBB Business Review of this Computers - Supplies & Parts in Whittier CA"
                            style="border: 0;" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/blue-seal-newegginc.png" />
                    </a>
                <script type="text/javascript" src="https://sealserver.trustwave.com/seal.js?code=337bdba159684b989be28d750101ed87"></script><a href="//www.newegg.com/Info/Awards.aspx" class="noline"
                    rel="nofollow">
                    <img src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/inc500.gif" style="border: 0;" alt="Inc500"></a><span id="gtrust_badges"></span>
                
        </div>
    </footer>
    <!--footer area end-->
    <div class="footer-disclaimer">
        
                    <a href="https://kb.newegg.com/Article/Index/12/3?id=1165" rel="nofollow">
                        Policy &amp; Agreement
                    </a>| <a href="https://kb.newegg.com/Article/Index/12/3?id=1166" rel="nofollow">
                        Privacy Policy
                    </a>
                
        &nbsp;
		&nbsp;<span id="ieFontCheck" style="width:0px;">A</span>ll rights reserved.
    </div>
    <div id="overlay" class="v655" style="display: none;">
    </div>
    <div id="modal" class="v655" style="display: none;">
        <span class="atnIcon icnInfo">
            <img alt="More Information" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/none.gif" /></span> <a class="atnIcon icnClose"
                href="javascript:void();" onclick="display.closeModal();">
                <img alt="close" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/none.gif" />Close</a>
        <div class="content">
        </div>
        <img style="display: none;" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/loading16.gif" alt="loading" />
    </div>
    
        <div class="v660">
            <div id="modalCommon" style="display: none;">
                <span class="atnIcon icnInfoNew" id="AlarmPanelNewCommon">
                    <img class="iconNew" alt="" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/none.gif" />
                    <span class="title"></span></span><a class="atnIcon icnCloseNew" href="javascript:void(0);"
                        onclick="Biz.Common.CommonPop.closePopup();">
                        <img alt="close window" src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/none.gif" /></a>
                <div class="content popUpLink" id="modalContent">
                </div>
                <div class="footer">
                    <a href="javascript:void(0);" onclick="Biz.Common.CommonPop.closePopup();">
                        close window
                    </a>
                </div>
            </div>
        </div>
    
<img src="//c1.neweggimages.com/WebResource/Themes/2005/Nest/Gomeznone7.gif" alt="" title="" width="0" height="0" />
<span style="display: none;">
    If the Adobe Reader does not appear when you click on a link for a PDF file, you can <a href='https://www.adobe.com/products/acrobat/readstep.html'>download Adobe Reader from the Adobe web site</a>.
</span>
<script type="text/javascript">
    jQuery(document).ready(function () { Biz.Common.PageFooter.setLink(); });
</script>

    <!-- end: footer -->

    
<script language="javascript">      function storeSREDID() {var thirtyDays=(60*60*1000*24)*30;var vals=document.location.search;start=vals.indexOf("SREDID=");if (start!=-1) {var end=vals.indexOf("&", start);if (end==-1){ end=vals.length; }var date=new Date();date.setTime(date.getTime()+ thirtyDays);document.cookie=vals.substring(start,end)+"; expires="+date.toGMTString()+"; path=/";}}function getSREDID(){var n="SREDID=";var cookies=document.cookie;var start=cookies.indexOf(n);if (start==-1){ return null; }start += n.length ;var end=cookies.indexOf(";", start);if (end==-1){ end=cookies.length; }return cookies.substring(start, end);}storeSREDID();      </script>





<!-- BEGIN SiteCatalyst --><script type='text/javascript'>jQuery(document).ready(function () {var parms=[];var re1 = new RegExp('(\\?|&)?icid=([^&]*)');jQuery('a').each(function (n) {var m_name = re1.exec(jQuery(this).attr('href'));if (m_name!=null) { parms.push(m_name[2]);}});if (parms.length>0) {Biz.Common.SiteCatalyst.sendForOnClick({ 'prop21': parms.join(",")}, 'banner impression');}})</script><script type='text/javascript' >var scp=typeof(scp)=='undefined'?{}:scp;scp.cmPageName="cat\x3a\x7bVideo Cards \x26 Video Devices\x7d";scp.serverName="E11WEB07";scp.pageType="Browsing;Store Browsing";scp.pageName="Home \x3e Components \x3e Video Cards \x26 Video Devices\x3acat";scp.searchKeyWord="video cards";scp.searchResult="redirect";scp.searchType="redirect";scp.tabStore="Components";scp.categoryStore="Video Cards \x26 Video Devices";scp.moreThan3level=false;scp.pageNickName="cat";Biz.Common.SiteCatalyst.send(scp);</script><!-- END SiteCatalyst -->










				<!-- BEGIN: Google Trusted Store -->
					<script type="text/javascript">
					  var gts = gts || [];
									 
					  gts.push(["id", "69025"]);
					  gts.push(["google_base_offer_id", ""]);
					  gts.push(["google_base_subaccount_id","8277688"]);
					  gts.push(["google_base_country","US"]);
					  gts.push(["google_base_language","en"]);
	          gts.push(["gtsContainer","gtrust_badges"]); 

					  (function() {
						var scheme = (("https:" == document.location.protocol) ? "https://" : "http://");
						var gts = document.createElement("script");
						gts.type = "text/javascript";
						gts.async = true;
						gts.src = scheme + "www.googlecommerce.com/trustedstores/gtmp_compiled.js";
						var s = document.getElementsByTagName("script")[0];
						s.parentNode.insertBefore(gts, s);
					  })();
					</script>
				<!-- END: Google Trusted Store -->
			



      <script type='text/javascript'>
      var utag_data = {
      page_breadcrumb:'Home &gt; Components &gt; Video Cards &amp; Video Devices',
            page_tab_name:'Components',
            page_category_name:'Video Cards &amp; Video Devices',
            page_number:'0',
            product_organic_skus:['3755779','N82E16814487291','N82E16814137054'],
            search_keyword:'video cards',
            page_type:'Category',
            page_store_name:'CategoryStore',
            site_region:'USA',
            site_currency:'USD',
            page_name:'StoreCategory',
            search_scope:jQuery('#haQuickSearchStore option:selected').text(),
            user_nvtc:Web.StateManager.Cookies.get(Web.StateManager.Cookies.Name.NVTC),
            user_name:Web.StateManager.Cookies.get(Web.StateManager.Cookies.Name.LOGIN,'LOGINID6'),
            third_party_render:['65531e14b4d9b9a223cc3bfcb65ce7b5f356011d','2a5e772a0f941c862180037f8a5c118c7abf2f7d']
            
      };
      </script>
      <script type='text/javascript'>
      (function(a,b,c,d){
          a='//tags.tiqcdn.com/utag/newegg/newegg.com/prod/utag.js';
          b=document;
          c='script';
          d=b.createElement(c);
          d.src=a;
          d.type='text/java'+c;
          d.async=true;
          a=b.getElementsByTagName(c)[0];
          a.parentNode.insertBefore(d,a)
      })();
      </script>
     
      


<script type='text/javascript'>var store_data={storeTypeInt:'1',
storeType:'category',
storeID:'38',
};</script>

    
    
    <script type="text/javascript">_satellite.pageBottom();</script>
</body>
</html>
'''

# Descomentar
#uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"item-container"})

filename = "productos.csv"

f = open(filename, "w")

headers = "brand,product_name\n"

f.write(headers)
# Para Tracear
i=0
for container in containers:
	brand = container.findAll("div",{"class":"item-branding"})
	title_container = container.findAll("a",{"class":"item-title"})
	product_name = title_container[0].text.strip()
	# La Marca la sacamos del title de una imagen
	if brand:
		brand = brand[0].a.img['title']
	else:
		# Si no esta el elemento con la marca saco la primera palabra del product name
		brand=product_name.split(' ')[0]
	
	print("brand " + str(i) + ": " + brand)
	print("product_name "+ str(i) + ": " + product_name)
	f.write(brand + "," + product_name +"\n")
	i=i+1
	
f.close()