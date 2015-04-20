<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="Xenon Boostrap Admin Panel" />
    <meta name="author" content="" />
    
    <title>Graph</title>

    <link rel="stylesheet" href="http://fonts.useso.com/css?family=Arimo:400,700,400italic">
    <link rel="stylesheet" href="assets/css/fonts/linecons/css/linecons.css">
    <link rel="stylesheet" href="assets/css/fonts/fontawesome/css/font-awesome.min.css">
    <link rel="stylesheet" href="assets/css/bootstrap.css">
    <link rel="stylesheet" href="assets/css/xenon-core.css">
    <link rel="stylesheet" href="assets/css/xenon-forms.css">
    <link rel="stylesheet" href="assets/css/xenon-components.css">
    <link rel="stylesheet" href="assets/css/xenon-skins.css">
    <link rel="stylesheet" href="assets/css/custom.css">


    <script src="assets/js/jquery-1.11.1.min.js"></script>
   	<script type="text/javascript" src="jquery.js"></script>
    <script type="text/javascript" src="jquery.flot.js"></script>
    <script>
    var options = {
            series: {
                lines: {
                    show: true
                },
                points: {
                    radius: 3,
                    fill: true,
                    show: true
                }
            },
            yaxes: [{
                axisLabel: "Gold Price(USD)",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 12,
                axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 3,

            }, {
                position: "right",
                axisLabel: "Change(%)",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 12,
                axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 3
            }
          ],
            legend: {
                noColumns: 0,
                labelBoxBorderColor: "#000000",
                position: "nw"
            },
            grid: {
                hoverable: true,
                borderWidth: 2,
                borderColor: "#633200",
                backgroundColor: { colors: ["#ffffff", "#EDF5FF"] }
            },
            colors: ["#FF0000", "#0022FF"]
        };
 
 
    $(function() {
        $.getJSON("/fetch",function(data){
            $(document).ready(function() {
                  $.plot($("#graphholder"), data, options);
            });
        });
    });

    jQuery(document).ready(function($)
    {   
        // Resize charts
        $(window).on('xenon.resize', function()
        {
            $("#map").render();
        });
    });
    </script>

</head>
<body class="page-body">
    <div class="settings-pane">
            
        <a href="#" data-toggle="settings-pane" data-animate="true">
            &times;
        </a>
        
        <div class="settings-pane-inner">
            
            <div class="row">
                
                <div class="col-md-4">
                    
                    <div class="user-info">
                        
                        <div class="user-image">
                            <a href="extra-profile.html">
                                <img src="assets/images/user-1.png" class="img-responsive img-circle" />
                            </a>
                        </div>
                        
                        <div class="user-details">
                            
                            <h3>
                                <a href="extra-profile.html">{{user_info[1]}}</a>
                                <!-- Available statuses: is-online, is-idle, is-busy and is-offline -->
                                <span class="user-status is-online"></span>
                            </h3>
                            
                            <p class="user-title">Administrator</p>
                            
                            <div class="user-links">
                                <a href="TBD" class="btn btn-primary">Edit Profile</a>
                                <a href="TBD" class="btn btn-success">Upgrade</a>
                            </div>
                            
                        </div>
                        
                    </div>
                    
                </div>
                
                <div class="col-md-8 link-blocks-env">
                    
                    <div class="links-block left-sep">
                        <h4>
                            <span>TBD</span>
                        </h4>
                        
                        <ul class="list-unstyled">
                            <li>
                                <input type="checkbox" class="cbr cbr-primary" checked="checked" id="sp-chk1" />
                                <label for="sp-chk1">TBD</label>
                            </li>
                            <li>
                                <input type="checkbox" class="cbr cbr-primary" checked="checked" id="sp-chk2" />
                                <label for="sp-chk2">TBD</label>
                            </li>
                            <li>
                                <input type="checkbox" class="cbr cbr-primary" checked="checked" id="sp-chk3" />
                                <label for="sp-chk3">TBD</label>
                            </li>
                            <li>
                                <input type="checkbox" class="cbr cbr-primary" checked="checked" id="sp-chk4" />
                                <label for="sp-chk4">TBD</label>
                            </li>
                        </ul>
                    </div>
                    
                    <div class="links-block left-sep">
                        <h4>
                            <a href="#">
                                <span>TBD</span>
                            </a>
                        </h4>
                        
                        <ul class="list-unstyled">
                            <li>
                                <a href="#">
                                    <i class="fa-angle-right"></i>
                                    TBD
                                </a>
                            </li>
                            <li>
                                <a href="#">
                                    <i class="fa-angle-right"></i>
                                    TBD
                                </a>
                            </li>
                            <li>
                                <a href="#">
                                    <i class="fa-angle-right"></i>
                                    TBD
                                </a>
                            </li>
                            <li>
                                <a href="#">
                                    <i class="fa-angle-right"></i>
                                    TBD
                                </a>
                            </li>
                        </ul>
                    </div>
                    
                </div>
                
            </div>
        
        </div>
        
    </div>
    <div class="copyrights"><a href="http://" title="copyrights">MongoDB University</a></div>
    <div class="page-container"><!-- add class "sidebar-collapsed" to close sidebar by default, "chat-visible" to make chat appear always -->
            
        <!-- Add "fixed" class to make the sidebar fixed always to the browser viewport. -->
        <!-- Adding class "toggle-others" will keep only one menu item open at a time. -->
        <!-- Adding class "collapsed" collapse sidebar root elements and show only icons. -->
        <div class="sidebar-menu toggle-others fixed collapsed">
            <div class="sidebar-menu-inner">    
                <header class="logo-env">
                    <!-- logo -->
                    <div class="logo">
                        <a href="/" class="logo-expanded">
                            <img src="assets/images/mongoDB.png" width="150" alt="" />
                        </a>
                        
                        <a href="/" class="logo-collapsed">
                            <img src="assets/images/mongoDB-collapsed.png" width="50" alt="" />
                        </a>
                    </div>
                    %if user_info[0] != False:
                    <div class="settings-icon">
                        <a href="#" data-toggle="settings-pane" data-animate="true">
                            <i class="linecons-cog"></i>
                        </a>
                    </div>
                    %end
                                
                </header>                   
                        
                <ul id="main-menu" class="main-menu">
                    <li>
                        <a href="conditional_search.html">
                            <i class="linecons-cloud"></i>
                            <span class="title">Conditional Search</span>
                        </a>
                    </li>
                    <li>
                        <a href="/graph">
                            <i class="linecons-star"></i>
                            <span class="title">Statistic</span>
                        </a>
                    </li>
                    <li>
                        <a href="charts-main.html">
                            <i class="linecons-globe"></i>
                            <span class="title">Map</span>
                        </a>
                    </li>
                    <li>
                        <a href="mailbox-main.html">
                            <i class="linecons-mail"></i>
                            <span class="title">Mailbox</span>
                            <span class="label label-success pull-right">5</span>
                        </a>
                        <ul>
                            <li>
                                <a href="mailbox-main.html">
                                    <span class="title">Inbox</span>
                                </a>
                            </li>
                            <li>
                                <a href="mailbox-compose.html">
                                    <span class="title">Compose Message</span>
                                </a>
                            </li>
                            <li>
                                <a href="mailbox-message.html">
                                    <span class="title">View Message</span>
                                </a>
                            </li>
                        </ul>
                    </li>
                    <li>
                        <a href="tables-basic.html">
                            <i class="linecons-database"></i>
                            <span class="title">Database</span>
                        </a>
                        <ul>
                            <li>
                                <a href="tables-basic.html">
                                    <span class="title">Basic Tables</span>
                                </a>
                            </li>
                            <li>
                                <a href="tables-responsive.html">
                                    <span class="title">Responsive Table</span>
                                </a>
                            </li>
                            <li>
                                <a href="tables-datatables.html">
                                    <span class="title">Data Tables</span>
                                </a>
                            </li>
                        </ul>
                    </li>
                    <li>
                        <a href="extra-gallery.html">
                            <i class="linecons-beaker"></i>
                            <span class="title">Extra</span>
                            <span class="label label-purple pull-right hidden-collapsed">New Items</span>
                        </a>
                        <ul>
                            <li>
                                <a href="extra-icons-fontawesome.html">
                                    <span class="title">Icons</span>
                                    <span class="label label-warning pull-right">4</span>
                                </a>
                                <ul>
                                    <li>
                                        <a href="extra-icons-fontawesome.html">
                                            <span class="title">Font Awesome</span>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="extra-icons-linecons.html">
                                            <span class="title">Linecons</span>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="extra-icons-elusive.html">
                                            <span class="title">Elusive</span>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="extra-icons-meteocons.html">
                                            <span class="title">Meteocons</span>
                                        </a>
                                    </li>
                                </ul>
                            </li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
        <div class="main-content">
                    
            <!-- User Info, Notifications and Menu Bar -->
            <nav class="navbar user-info-navbar" role="navigation">
                
                <!-- Left links for user info navbar -->
                <ul class="user-info-menu left-links list-inline list-unstyled">
                    
                    <li class="hidden-sx hidden-xs">
                        <a href="#" data-toggle="sidebar">
                            <i class="fa-bars"></i>
                        </a>
                    </li>
                    <!-- message -->
                    <li class="dropdown hover-line">
                        <a href="#" data-toggle="dropdown">
                            <i class="fa-envelope-o"></i>
                            <span class="badge badge-blue">1</span>
                        </a>
                            
                        <ul class="dropdown-menu messages">
                            <li>
                                    
                                <ul class="dropdown-menu-list list-unstyled ps-scrollbar">
                                
                                    <li class="active"><!-- "active" class means message is unread -->
                                        <a href="#">
                                            <span class="line">
                                                <strong>Luc Chartier</strong>
                                                <span class="light small">- yesterday</span>
                                            </span>
                                            
                                            <span class="line desc small">
                                                This ain’t our first item, it is the best of the rest.
                                            </span>
                                        </a>
                                    </li>
                                    
                                    <li>
                                        <a href="#">
                                            <span class="line">
                                                Hayden Cartwright
                                                <span class="light small">- a week ago</span>
                                            </span>
                                            
                                            <span class="line desc small">
                                                Whose her enjoy chief new young. Felicity if ye required likewise so doubtful.
                                            </span>
                                        </a>
                                    </li>
                                </ul>
                                
                            </li>
                            
                            <li class="external">
                                <a href="blank-sidebar.html">
                                    <span>All Messages</span>
                                    <i class="fa-link-ext"></i>
                                </a>
                            </li>
                        </ul>
                    </li>
                    <!-- notification -->
                    <li class="dropdown hover-line">
                        <a href="#" data-toggle="dropdown">
                            <i class="fa-bell-o"></i>
                            <span class="badge badge-purple">3</span>
                        </a>
                            
                        <ul class="dropdown-menu notifications">
                            <li class="top">
                                <p class="small">
                                    <a href="#" class="pull-right">Mark all Read</a>
                                    You have <strong></strong> new notifications.
                                </p>
                            </li>
                            
                            <li class="external">
                                <a href="#">
                                    <span>View all notifications</span>
                                    <i class="fa-link-ext"></i>
                                </a>
                            </li>
                        </ul>
                    </li>   
                </ul>
                <!-- Right links for user info navbar -->
                <ul class="user-info-menu right-links list-inline list-unstyled">
                    
                    <li class="search-form">
                        
                        <form method="get" action="TBD">
                            <input type="text" name="s" class="form-control search-field" placeholder="Type to search..." />
                            
                            <button type="submit" class="btn btn-link">
                                <i class="linecons-search"></i>
                            </button>
                        </form>
                    </li>
                    %if user_info[0] == False:
                    <li >
                        <a class="text-bold" id="login" href="#" data-toggle="modal" data-target="#myModal">Login</a>
                    </li>
                    <li>
                        <a class="text-bold" id="register" href="#" data-toggle="modal" data-target="#myModal">register</a>
                    </li>
                    %else:
                    <li class="dropdown user-profile">
                        <a href="#" data-toggle="dropdown">
                            <img src="assets/images/user-1.png" alt="user-image" class="img-circle img-inline userpic-32" width="35" />
                            <span>
                                {{user_info[1]}}
                                <i class="fa-angle-down"></i>
                            </span>
                        </a>
                        
                        <ul class="dropdown-menu user-profile-menu list-unstyled">
                            <li>
                                <a href="#edit-profile">
                                    <i class="fa-edit"></i>
                                    New Post
                                </a>
                            </li>
                            <li>
                                <a href="#settings">
                                    <i class="fa-wrench"></i>
                                    Settings
                                </a>
                            </li>
                            <li>
                                <a href="#profile">
                                    <i class="fa-user"></i>
                                    Profile
                                </a>
                            </li>
                            <li>
                                <a href="#help">
                                    <i class="fa-info"></i>
                                    Help
                                </a>
                            </li>
                            <li class="last">
                                <a >
                                    <i class="fa-lock"></i>
                                    Logout
                                </a>
                            </li>
                        </ul>
                    </li>
                    %end
                </ul>
                
            </nav> 
        
        <div  align="center">
            <div id="graphholder" style="width:600px;height:300px"></div>
            <br><br><br>
            <div id="parameters"></div>
        </div>

        <form method='post'>
        <div class="row">
            <div class="col-sm-4">
            Place One: 
            <select class="form-control" name="place_name1"> 
            <table>
                %for option in PlaceOptions:
                <tr>
                <option>{{option}}</option>
                </tr>
                %end
            </table>
            </select>
            <br>

            Start Data<input class="form-control" type="text" name="start_date1" value="20150106"/><br>
            End Data<input class="form-control" type="text" name="end_date1" value="20150120"/>
            </div>

            <div class="col-sm-4">
            Place Two: 
            <select class="form-control" name="place_name2"> 
            <table>
            %for option in PlaceOptions:
            <tr>
                <option>{{option}}</option>
            </tr>
            %end
            </table>
            </select>
            <br>
            Start Data<input class="form-control" type="text" name="start_date2" value="20150106"/><br>
            End Data<input class="form-control" type="text" name="end_date2" value="20150120"/><br>
            </div>

            <div class="col-sm-2">
            Data Type<br>
            <div class="row">
                <div class="col-sm-5">
                <input class="form-control" type="radio" name="data_type" value="TMAX" checked="true"/>TMAX
                <input class="form-control" type="radio" name="data_type" value="TMIN"/>TMIN
                </div>
                <div class="col-sm-5">
                    <input class="form-control" type="radio" name="data_type" value="PRCP"/>PRCP
                    <input class="form-control" type="radio" name="data_type" value="SNWD"/>SNWD
                </div>
            </div>
            </div>

            <div class="col-sm-2">
                <br><br><br><br><br>
                <input class="form-control" type='submit' value='Analyse'>
            </div>
        </div>
        </form>

                    <!-- Main Footer -->
            <footer class="main-footer sticky footer-type-1">
                
                <div class="footer-inner">
                
                    <!-- Add your copyright text here -->
                    <div class="footer-text">
                        &copy; 2015 
                        <a href="http://" target="_blank" title="mongoDB"><strong>MongoDB University</strong> </a>
                    </div>
                
                    <div class="go-up">
                        <a href="#" rel="go-top">
                            <i class="fa-angle-up"></i>
                        </a>
                    </div>
                </div>
            </footer>
        </div>
    </div>
    
    <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">
                          &times;
                    </button>
                    <h4 class="modal-title" id="myModalLabel">Login</h4>
                </div>
                <div class="modal-body">
                    <form id="login_form" action="/login" method="post">
                        Username:<input id="username" name="username" type="text" />
                        Password:<input id="password" name="password" type="password" />
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">
                        close
                    </button>
                    <button id="confirm" type="submit" class="btn btn-primary" form="login_form">
                        confirm
                    </button>
                </div>
             </div><!-- /.modal-content -->
        </div><!-- /.modal -->
    </div>

    <div class="page-loading-overlay">
        <div class="loader-2"></div>
    </div>

    <!-- Bottom Scripts -->
    <script src="assets/js/bootstrap.min.js"></script>
    <script src="assets/js/TweenMax.min.js"></script>
    <script src="assets/js/resizeable.js"></script>
    <script src="assets/js/joinable.js"></script>
    <script src="assets/js/xenon-api.js"></script>
    <script src="assets/js/xenon-toggles.js"></script>


    <!-- Imported scripts on this page -->
    <script src="assets/js/xenon-widgets.js"></script>
    <script src="assets/js/devexpress-web-14.1/js/globalize.min.js"></script>
    <script src="assets/js/devexpress-web-14.1/js/dx.chartjs.js"></script>
    <script src="assets/js/toastr/toastr.min.js"></script>


    <!-- JavaScripts initializations and stuff -->
    <script src="assets/js/xenon-custom.js"></script>

    </body>
</html>