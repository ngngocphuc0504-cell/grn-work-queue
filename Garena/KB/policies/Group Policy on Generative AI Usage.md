# **Group Policy on GenAI Usage**

*Last Updated: 25 May 2026* 

This **Group Policy on Generative AI Usage** establishes a baseline for the responsible use of Generative AI (“GenAI”) within Sea Limited and its subsidiaries (“the Company”). 

We firmly believe in the potential of new technology such as GenAI to drive innovation, growth, and excellence within the Company. Through this policy, we hope to provide more clarity on how GenAI can be used responsibly, in order to support its adoption and benefits. 

**Table of Contents**

[**1\. Introduction	1**](#1.-introduction)

[**2\. Scope and Definitions	1**](#2.-scope-and-definitions)

[**3\. Responsible Use	2**](#3.-responsible-use)

[3.1 Guiding Principles	2](#3.1-guiding-principles)

[3.2 Prohibited Uses of GenAI	3](#3.2-prohibited-uses-of-genai)

[3.3 Recommended Uses of GenAI	3](#3.3-recommended-uses-of-genai)

[**4\. Governance Processes	3**](#4.-governance-processes)

[4.1 Whitelisting GenAI Tools for Handling Proprietary Information	3](#4.1-whitelisting-genai-tools-for-handling-proprietary-information)

[4.2 Requesting for Third-Party GenAI APIs	4](#4.2-requesting-for-third-party-genai-apis)

[**5\. Legal Considerations	4**](#5.-legal-considerations)

[**6\. Policy Compliance	5**](#6.-policy-compliance)

[6.1 Incident Management and Escalation	5](#6.1-incident-management-and-escalation)

[6.2 Policy Violations and Enforcement	5](#6.2-policy-violations-and-enforcement)

[6.3 Policy Review	6](#6.3-policy-review)

[**7\. Disclaimers	6**](#7.-disclaimers)

## 

## **1\. Introduction** {#1.-introduction}

This policy serves as a common baseline for the responsible use of GenAI within the Company. It is meant to ensure that GenAI tools are used in a way that aligns with the Company’s values whilst managing its potential risks. Individual business units and departments are free to enact their own additional governance processes, usage guidelines and best practices on top of this foundational policy.  

This policy should be read alongside applicable Corporate IT, information security, Legal AI Review, procurement, and LLM Gateway requirements, as well as any entity-specific compliance obligations. Where those requirements are more specific, they take precedence.

The policy distinguishes between user-level GenAI tools, internally developed or self-hosted GenAI systems, AI coding / developer tools, and GenAI APIs or models. Each category may have different approval, data, and technical control requirements.

## **2\. Scope and Definitions**  {#2.-scope-and-definitions}

This policy applies to all employees, contractors, and third parties acting on behalf of or in the interest of the Company who use GenAI tools in the course of their work (“users”). It is in addition to any existing company policies that users are expected to follow (e.g. employee code of conduct). Any requests for exceptions or deviations from this policy should be directed to [GenAI@sea.com](mailto:GenAI@sea.com).

**Generative AI** refers to a type of Artificial Intelligence (“AI”) that can generate new content, such as text, images, audio, video, and code, based on patterns learned from existing data. Unlike other legacy forms of machine learning, which primarily classifies or predicts based on input data, GenAI creates novel outputs by leveraging deep learning models, particularly neural networks like transformers and diffusion models. 

**GenAI Tools** are applications, platforms, or software that leverage GenAI to create new content, such as text, images, audio, video, and code. Such tools may be internally developed or from third-parties, and include chatbots, coding assistants, and content generators for image, audio and video. Some examples of third-party GenAI Tools can be found **below**.

| Output Created | Examples of Third-Party GenAI Tools |
| :---: | :---- |
| Text | ChatGPT, Gemini, Claude |
| Image | DALL.E, Adobe Firefly, Stable Diffusion |
| Audio | Jukebox, ElevenLabs, Boomy |
| Video | Synthesia, Runway ML, DeepBrain AI |
| Code | Claude Code, Codex, Cursor, GitHub Co-Pilot |

## 

## **3\. Responsible Use** {#3.-responsible-use}

### **3.1 Guiding Principles** {#3.1-guiding-principles}

The responsible use of GenAI within the Company is based on the **following** guiding principles:

1. **Accountability**  
* Users and their managers are fully accountable for their use of AI-generated content and are expected to apply their best judgement in their application.  
* For one-off uses of GenAI, the AI-generated content should undergo human review before being used for decision-making or external purposes.  
* For repeated or systematic uses of GenAI (where human-in-the-loop review may not always be feasible or is counterproductive), the underlying repeated process or system, its outputs, and its safeguards should be thoroughly reviewed upfront  to manage any potential risks from its use (e.g. in terms of accountability,  reliability, security, privacy, compliance, accuracy, and bias).  
* Consult your management if there is any doubt on the above.

2. **Security and Privacy**  
* Users of GenAI tools should only upload proprietary information (e.g. sensitive and/or confidential information) to [Whitelisted GenAI Tools](#4.1-whitelisting-genai-tools-for-handling-proprietary-information) which have been evaluated by the Company for data security and privacy risks.  
* Users must always comply with the data security and privacy protocols applicable to their business to prevent data breaches, unauthorized access, or misuse.  
* Consult the Corporate IT department if there is any doubt on the above. 

3. **Compliance and Disclosure**  
* All GenAI tools must be used in accordance with the law. This is on top of any prevailing company policies governing their use. Users should also adequately document their use of GenAI tools for compliance and audit purposes.  
* Any AI-generated content must respect intellectual property (“IP”) and personal rights. For example, users should not make use of GenAI to replicate individuals’ voices, appearances, or artistic styles without those individuals’ consent.  
* Steps should be taken to disclose when content is AI-generated to audiences that do not expect GenAI to be used.   
* Refer to the section on [Legal Considerations](#5.-legal-considerations) for more details. Consult the Legal department if there is any doubt on the above. 

4. **Accuracy and Bias**  
* Users should ensure that AI-generated content is accurate, appropriate,  non-misleading, and with care exercised to control for systematic bias.  
* Consult your management if there is any doubt on the above.

5. **Continuous Improvement**  
* GenAI enabled workflows should be regularly reviewed to ensure that they stay up-to-date with the rapidly evolving technology, business, and legal landscape.   
* Users that regularly make use of GenAI tools in their work should seek to continuously educate themselves on the latest solutions, risks, and best practices to ensure both responsible and effective use.

### **3.2 Prohibited Uses of GenAI** {#3.2-prohibited-uses-of-genai}

## Users must not use GenAI tools for:

1. Creating or disseminating false, deceptive or harmful content (e.g. deepfakes, malicious code, and explicit content);  
2. Activities that violate legal regulations including IP rights and personal data protection laws, such as by sharing users’ personal information with external GenAI tools;  
3. Using GenAI to maliciously bypass any existing company workflows or security protocols; and 

Performing actions that run counter to the best interests and values of the Company.Users must also not use GenAI tools, accounts, models, APIs, or browser extensions to bypass Company’s procurement processes, approvals, data security, access-control, budget controls or LLM Gateway processes (if applicable).

Users must not use personal API keys, personal paid accounts, unmanaged SaaS tools, or non-whitelisted GenAI tools for Company proprietary information, production workflows, external customer-facing use, or regulated-entity use.

The above is not an exhaustive list. If in doubt, check with your management on whether the intended use case aligns with the Company’s [Guiding Principles](#3.1-guiding-principles) on GenAI usage.

### **3.3 Recommended Uses of GenAI**  {#3.3-recommended-uses-of-genai}

Users may consider using GenAI tools for tasks such as, but not limited to:

1. Creating initial drafts of content (e.g. emails, reports, presentations, storyboards, and mock-ups);   
2. Conducting research and analysis to inform decision-making (e.g. distilling of information, identification of data trends, and generation of insights);  
3. Brainstorming for ideas or creative solutions;   
4. Automating parts of a business process that is repetitive, predictable, and/or mundane;   
5. Generating initial code or debugging existing code; and  
6. Language translation.

The above is not meant to be an exhaustive list, and users are encouraged to experiment on innovative use cases with their teams and departments. 

## **4\. Governance Processes** {#4.-governance-processes}

### **4.1 Whitelisting GenAI Tools for Handling Proprietary Information** {#4.1-whitelisting-genai-tools-for-handling-proprietary-information}

Whitelisting is the process of formally evaluating and designating a GenAI tool for the handling of proprietary information. Only whitelisted GenAI tools should be used if sensitive and/or confidential information have to be uploaded or inputted, as these tools would have been evaluated by the Company to manage potential data security risks.

All internally developed and self-hosted GenAI tools are considered whitelisted so long as they are approved through the business or department’s usual software development requesting process. 

Third-party GenAI tools are procured and whitelisted centrally by the Corporate IT department. Information on currently whitelisted GenAI tools can be found in the Knowledge section of [IT Center](https://itcenter.sea.com/) (IT Centre \>\> Top Bar: “Knowledge” \>\> Side Bar: “Software Licenses”). Users can also submit new third-party GenAI Tools for procurement and whitelisting through the [IT Center](https://itcenter.sea.com/):

| Use Case for GenAI Tool | Request Type |
| :---- | :---- |
| For handling of proprietary information  | Whitelist Software |
| For sandbox testing with non-proprietary information | Other Software Request |

###  **4.2 Requesting for Third-Party GenAI APIs** {#4.2-requesting-for-third-party-genai-apis}

Various first-party and third-party GenAI Application Programming Interfaces (APIs) exist with capabilities that can be integrated into Company systems, products and services. These are centrally procured and managed by the Company. Any requests for third-party GenAI APIs should be made through each business unit’s appointed API Coordinator(s):

| Business Unit | API Coordinator(s) | Email |
| :---- | :---- | :---- |
| Shopee / Monee | Wu Ziyang | [ziyang.wu@shopee.com](mailto:ziyang.wu@shopee.com) |
| Garena | Chen Yanlun | [yanlun.chen@garena.com](mailto:yanlun.chen@garena.com) |
| Sea | Yang Bo | [yangbo@sea.com](mailto:yangbo@sea.com) |

## **5\. Legal Considerations** {#5.-legal-considerations}

All users of GenAI tools should ensure that they comply with legal requirements around the use of AI. These could be based on public regulatory law, IP law, and/or private contract law with service providers of AI tools. The Legal teams of each business unit can provide relevant guidance on how these requirements apply to different businesses, jurisdictions and operating contexts. Some evergreen legal issues to consider include:

* **Avoid IP infringement.** When using AI to generate new content it is necessary to avoid using prompts that suggest an effort to deliberately infringe the IP of a third party, including trademarks, copyrights, or personality rights of individuals such as models or voice actors that have not consented to the use of their likeness for AI training.  
* **Ensure IP protection.** Rules are unsettled on whether any material generated by AI is entitled to IP protection. As such, any AI generated material which the company has an interest in obtaining IP protection for runs the risk that third parties may freeride or copy our valuable IP. IP protections are highest for materials made by human creators, with GenAI usage limited as an inspirational or brainstorming tool. Users of GenAI tools for creative purposes should maintain documentary evidence of the role that GenAI tools play in the creative process, and the human contributions to the production process.  
* **Comply with data protection laws.** Only use personal data with GenAI that has been vetted for compliance with data protection laws such as the Personal Data Protection Act (PDPA) in Singapore and the General Data Protection Regulation (GDPR) in the European Union. These impose strict conditions on how personal identifying data is used, processed, and transferred. The act of providing identifying personal information to an external AI platform or service needs to be verified for compliance.  
* **Mind restrictions on commercial use.** Not all AI tools are approved for commercial use, and many activities undertaken by the Company may be deemed as “commercial use” even if it is for purely internal use cases.   
* **Avoid prohibited purposes.** Do not use AI for prohibited purposes. [Section 3.2](#3.2-prohibited-uses-of-genai) of this document provides helpful guideposts, but these rules are constantly evolving and different use cases may be prohibited under specific countries' AI use guidelines.  
* **Document  usage of GenAI.** Users should adequately document their use of GenAI tools for compliance and audit purposes. These should be in accordance with the Company’s prevailing data retention policies. This could include but is not limited to documentation relating to foundation models used, data sources, input prompts, model outputs, and access logs.

Users should consult the Legal department for guidance on specific compliance with local regulations and standards, especially if there is any doubt on the above. 

For GenAI APIs, new models, preview models, external-facing use cases, customer data, personal data, regulated-entity data, or production workflows, Legal AI Review will assess model terms, data usage and retention terms, customer-data restrictions, geography restrictions, commercial-use rights, prohibited-use restrictions, output disclosure requirements, and whether the requested use case is approved, restricted, or blocked. Legal approval should be recorded at the appropriate level: vendor / contract, model / model family, data class, use case, jurisdiction, and production or testing status. A prior vendor or contract review should not be treated as blanket approval for all future models or use cases.

## **6\. Policy Compliance** {#6.-policy-compliance}

### **6.1 Incident Management and Escalation**  {#6.1-incident-management-and-escalation}

Users are encouraged to remain vigilant and should notify the Company of any suspected or actual incidents involving GenAI that may harm the Company’s interests (e.g. suspicious or illegal activity, misuse, data leak, malware, systematic bias, bad publicity etc.).

Any incidents involving GenAI should be reported to the COO Office at [GenAI@sea.com](mailto:GenAI@sea.com).

### **6.2 Policy Violations and Enforcement** {#6.2-policy-violations-and-enforcement}

Failure to comply with this policy may result in disciplinary action, including termination of employment. Violations may also be reported by the Company to the relevant authorities if they involve unlawful activities. Examples of violations include, but are not limited to:

1. Using GenAI tools in a manner that contravenes the Company’s compliance obligations;  
2. Ignoring or bypassing policies and safeguards set by the Company for the responsible use of GenAI; and  
3. Deliberately misusing AI-generated content to harm or mislead others.

Any violations should be reported to the COO Office at [GenAI@sea.com](mailto:GenAI@sea.com).

### **6.3 Policy Review** {#6.3-policy-review}

This policy may be reviewed periodically to address the rapidly evolving technology, business, and legal landscape. Questions or feedback on this policy can be directed to Cheng Lee Chon ([chenglc@sea.com](mailto:chenglc@sea.com)) and Sharon Chan ([chansh@sea.com](mailto:chansh@sea.com)) from the COO Office.

## **7\. Disclaimers** {#7.-disclaimers}

This policy provides guidance on the responsible and compliant use of GenAI within the Company. While every effort has been made to ensure the accuracy and relevance of the information contained herein, this document does not constitute legal, regulatory, or technical advice. Users must exercise their own judgment and consult with their management, Legal, and/or Corporate IT department when in doubt regarding specific use cases.

The Company reserves the right to update, modify, or revoke this policy at any time in response to evolving technological, business, or legal requirements. Compliance with this policy does not exempt individuals or teams from additional regulatory obligations or internal compliance measures that may apply to their specific roles or jurisdictions.

The company assumes no liability for any unauthorized use of GenAI tools, failure to adhere to the prescribed guidelines, or any legal, reputational, or operational risks that may arise due to misuse or misinterpretation of AI-generated content. Users continue to remain individually responsible for ensuring that any AI-generated content that they create, process or handle aligns with the Company’s values, policies, and applicable laws.