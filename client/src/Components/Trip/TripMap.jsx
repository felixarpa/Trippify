import React, { Component } from 'react';
import { Box, Text } from 'grommet';
import './Trip.css';

class TripMap extends Component {
  render() {
    return(
      <Box className='not-yet'
        width='large'
        border={{ color: 'accent-1', size: 'small' }}
        margin={{top:'small', bottom:'large'}}
        pad="medium" 
        round='small'>
        <Text size='large'>
          <b>MAP</b>
        </Text>
        <Box><div className='maps'/></Box>
      </Box>
    );
  }
}

export default TripMap;