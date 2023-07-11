import React, { Component } from 'react';

class App extends Component {
    state = {
        posts: []
    };

    async componentDidMount() {
        try {
            const res = await fetch('http://127.0.0.1:8000/api/');
            const posts = await res.json();
            this.setState({
                posts
            });
        } catch (e) {
            console.log(e);
        }
    }

    render() {
        return (
              <div style={{padding:"12px"}}>
               

                    

                        <table border="2">
                        <colgroup>
                          <col width="10%" />
                          <col width="30%" />
                          <col width="40%" />
                          <col width="20%" />
                        </colgroup>

                        <thead>
                          <tr>
                              <th>ID</th>
                              <th>제목</th>
                              <th>내용</th>
                              <th>작성자</th>

                          </tr>

                        </thead>
                        {this.state.posts.map(item => (
                        <tbody>
                          <td>{item.id}</td>
                          <td>{item.title}</td>
                          <td>{item.content}</td>
                          <td>{item.writer}</td>
                        </tbody>
                     
                     ))}

                        </table>
                   
                
            </div>
        );
    }
}

export default App;