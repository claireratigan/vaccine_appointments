<!DOCTYPE html>
<html lang="en">

<head>
    <title>HEB Vaccine Tracker</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.1/css/bulma.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
</head>

<body>
    <!-- header -->
    <div class="hero-head">
        <section class="hero is-primary is-small" id="header">
            <div class="hero-body">
                <div class="container">
                    <div class="header-titles">
                        <h3 class="title is-3 is-spaced">HEB Vaccine Tracker</h3>
                    </div>
                    <div class="header-buttons">
                        <span class="control">
                            <a class="button is-dark is-clickable" href="https://github.com/TheIronicCurtain/vaccine_appointments">
                                <span class="icon">
                                    <i class="fa fa-github"></i>
                                </span>
                                <span>Github</span>
                            </a>
                        </span>
                    </div>
                </div>
            </div>
        </section>
    </div>
    <!-- end of header -->

    <!-- data content block -->
    <div class="content-block">
        <section class="hero">
            <div class="hero-body">
                <div class="container">
                    <div class="content">
                        <h4 class="title is-4 is-spaced"> {{loc.capitalize()}} Appointments</h4>
                        <div class="main-text">
                            %for row in data:
                            <div class="box">
                                <div class="columns is-mobile">
                                    <div class="column is-four-fifths">
                                        <div class="container center">
                                            <h1 class="title is-5" href="{{row['name']}}">{{row['name']}}</h1>
                                            <address class="subtitle is-7">
                                              {{row['street']}}, {{row['city']}} {{row['state']}} {{row['zip']}}
                                            </adress>
                                        </div>
                                    </div>
                                    <div class="column">
                                        <nav class="level">
                                            <div class="level-item has-text-centered">
                                              <div>
                                                <p class="heading "> Available Slots</p>
                                                <p class="title is-5">{{row['openTimeslots']}}</p>
                                              </div>
                                            </div>
                                        </nav>
                                    </div>
                                  </div>
                            </div>
                            %end
                        </div>

                    </div>
                </div>
            </div>
        </section>
    </div>
    <!-- end of data block -->

    <!-- footer -->
    <div class="hero-footer footer">
        <div class="container has-text-centered">
            <span class="icon">
                <i class="fa fa-github"></i>
            </span>
            <p>Template by <a>github.com/hobbs1210</a></p>
        </div>
    </div>
    <!-- end of footer -->
</body>

</html>