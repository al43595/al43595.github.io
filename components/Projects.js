import React from 'react';
import ProjectItem from './ProjectItem';

class Projects extends React.Component {
    state = {
        projects: [/* ... your hardcoded projects here ... */]
    };

    render() {
        return (
            <div>
                {this.state.projects.map(project => <ProjectItem key={project.id} details={project} />)}
            </div>
        );
    }
}

export default Projects;
