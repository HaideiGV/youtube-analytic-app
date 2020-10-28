import React from 'react';
import axios from 'axios';
import '../App.css';

class ChannelInfo extends React.Component {
    constructor(props) {
        super(props);
        this.state = {channelName: '', totalViews: 0, avgViews: 0};
    }

    componentDidMount() {
        let data = this.getChannelInfo();
        console.log(data);
    }

    getChannelInfo(event) {
        axios.get(
            'http://127.0.0.1:8000/api/channels?username=TheBadComedian'
        )
        .then(response => {
            this.setState(
                state => ({
                    channelName: response.data.channel_name,
                    totalViews: response.data.total_views,
                    avgViews: response.data.avg_views
                })
            )
        })
        .catch(function (error) {console.log(error);})
        .then(function () {});
    }

    render() {
        return (
            <div>
                <p>
                    Channel Name: <span>{this.state.channelName}</span>
                </p>
                <p>
                    Total Views: <span>{this.state.totalViews}</span>
                </p>
                <p>
                    Average Views: <span>{this.state.avgViews}</span>
                </p>
            </div>
        );
    }
}

export default ChannelInfo;
