# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Vayu Puran 0.721)
- **Original**: 75 स्थानाभिमानिनः सर्वे स्थानाख्याश्चेव ते समता: ।
- **Translation**: 

---

### Verse 2 (Vayu Puran 0.722)
- **Original**: 76 वक्‍्त्ायस्य ब्राह्मणाः संप्रसूतास्तद्क्षस्तः क्षत्रियाः पूर्व भागे । चैश्याश्रोधरर्यिस्य पदूम्यां च शूद्धाः सर्च चर्णा गात्रतः संप्रखूताः ।
- **Translation**: 

---

### Verse 3 (Vayu Puran 0.723)
- **Original**: 77 नारायण: परोडव्यक्तादण्डमव्यक्तसंमचम्‌ । अण्डाज्जशे पुनत्नल्या लोकास्तेन कताः स्वयम्‌
- **Translation**: 

---

### Verse 4 (Vayu Puran 0.724)
- **Original**: पथ: व कथितः पादः समासान्षतु विस्तरात्‌
- **Translation**: 

---

### Verse 5 (Vayu Puran 0.725)
- **Original**: अनेना5उद्येन पादेन पुराण संप्रकीतितम्‌
- **Translation**: 

---

### Verse 6 (Vayu Puran 0.726)
- **Original**: 7< इति महापुराणे वायुप्रोक्ते प्रक्रियापादे सृश्च्रिकरणं नाम पष्ठोष्ष्यायः ।6। समाप्तः प्रक्रियापादः । अथ सप्तमो5्ध्यायः प्जत्तिस्लैध्यिष्की लॉ ल्वकत्‌ +सूत उचाच इत्येष प्रथमः पादः प्रक्रियार्थः प्रकीतितः। श्र॒त्वा तु संहृष्टमनाः काश्यपेयः सनातन:
- **Translation**: 

---

### Verse 7 (Vayu Puran 0.727)
- **Original**: ।1 __ ख जलि-प-पपपपयय।पपयप।खपप ः कला, मुहत्त, सन्धि, राजि, दिन, पक्ष, मास, अपन, वर्ष, युग, ये सभी स्थानाभिमानी और स्थान के नाम से प्रसिद्ध हैं ।93-76। जिसके मुख से ब्राह्मण, वक्ष:स्थल से क्षत्रिय, ऊरु से वेश्य और जिसके पैर से शूद्र, इस प्रकार जिसके शरीर से सब वर्ण उत्पन्न हुए वे नारायण अव्यक्त से परे हैं। उत अव्यक्त से अण्ड की उत्पत्ति हुई और अण्ड से ब्रह्मा उत्पन्न हुए. जिन्होंने स्वयं लोकों को उत्पन्न किया। यह प्रक्रियापाद आप लोगों से संक्षेप में कहा गया है। इस प्रकार इस आद्य पांद के द्वारा यह पुराण कहा गया है
- **Translation**: 

---

### Verse 8 (Vayu Puran 0.728)
- **Original**: 97-79। श्री वायुपुराण का सृष्टि-प्रमाणनामक छरठाँ अध्याय समाप्त । 6
- **Translation**: 

---

### Verse 9 (Vayu Puran 0.729)
- **Original**: अध्याय 7 सूतजी बोले--यह पहला प्रक्रिग पाद कह दिया गया, जिसको सुनकर सनातन काश्यपेय प्रसन्न +इदं नास्ति क. पुस्तके ।
- **Translation**: 

---

### Verse 10 (Vayu Puran 0.730)
- **Original**: 96 ह वायुपुराणम «खंबोध्य सूते चचसो पश्रच्छाथोत्तरां कथाम्‌
- **Translation**: 

---

### Verse 11 (Vayu Puran 0.731)
- **Original**: अतः प्रश्ति कव्पज्ञ प्रतिसंधि प्रचद्य नः
- **Translation**: 

---

### Verse 12 (Vayu Puran 0.732)
- **Original**: 2 समतीतस्य कल्पस्य वरंमानस्य चोभयों; । कल्पयोरन्तर्र यज्य प्रतिसंधियेतस्तयोः । एतद्देद्तुमिच्छाम अ(मो हाय) त्यन्तकुशलो इह्यसि
- **Translation**: 

---

### Verse 13 (Vayu Puran 0.733)
- **Original**: 3 लोॉमहषेण उवाच थे अन्न वो56 प्रवक्ष्यामि प्रतिसंधिश्र यस्तयोः । समतीतस्थ कठ्पस्थ चर्तमानस्य चोभयोः:
- **Translation**: 

---

### Verse 14 (Vayu Puran 0.734)
- **Original**: 9 मन्वन्तराणि कव्पेषु येघु यानि च सुबताः
- **Translation**: 

---

### Verse 15 (Vayu Puran 0.735)
- **Original**: यश्ायं वर्तते कल्पो चाराहूः सांप्रतः शुभः
- **Translation**: 

---

### Verse 16 (Vayu Puran 0.736)
- **Original**: 5 अस्मात्कल्पात्च यः कल्पः पूर्वोंठतीतः सनातनः । तस्य चास्य च कल्पस्य मध्यादस्थां निबोधत
- **Translation**: 

---

### Verse 17 (Vayu Puran 0.737)
- **Original**: प्रत्याहते पूर्वकाले प्रतिसंधि च तत्न वै। अन्य; प्रचर्तते कल्पों जनाल्लोकात्पुनः पुनः
- **Translation**: 

---

### Verse 18 (Vayu Puran 0.738)
- **Original**: 7 व्यूच्छिन्नात्यतिसंधेस्तु कल्पाकहपः परस्परम्‌ । व्युच्छिद्न्ते
- **Translation**: 

---

### Verse 19 (Vayu Puran 0.739)
- **Original**: क्रियाःसर्चा: कल्पान्ते सचंशस्तदा तस्मात्कट्पाक्तु कल्पस्य प्रतिसंधिनिंगद्यते। मन्चन्तरयुगाख्यानामव्युच्छिन्नाश्य संघयः
- **Translation**: 

---

### Verse 20 (Vayu Puran 0.740)
- **Original**: < परस्पराः प्रवर्तन्ते मन्वन्तरथुगेः सह । उक्ता ये प्रक्तिया्थेंन पू्चकल्पा! समासतः
- **Translation**: 

---

