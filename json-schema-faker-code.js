
import { generate } from 'json-schema-faker';

const schema = {
    type: 'object',
    properties: {
        id: {
            type: 'integer',
            minimum: 1,
            maximum: 1000
        },
        name: {
            type: 'string',
            minLength: 5,
            maxLength: 20
        },
        age: {
            type: 'integer',
            minimum: 18,
            maximum: 65
        },
        email: {
            type: 'string',
            format: 'email'
        },
        active: {
            type: 'boolean'
        }
    },
    required: ['id', 'name', 'age', 'email']
};

const result = await generate(schema);

console.log(JSON.stringify(result, null, 2));
