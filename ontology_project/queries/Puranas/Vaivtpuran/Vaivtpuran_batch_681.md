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

### Verse 1 (Vaivtpuran 92.19299)
- **Original**: त्वमेव प्राक्तन॑ सर्व कृष्णं द्रक्ष्यसि साम्प्रतम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 92.19300)
- **Original**: त्वत्तो विश्व॑ पवित्र॑ च॒त्वत्पादरजसा मही । सुपतित्र॑ त्वद्दन॑ पुण्यवत्यश्ष गोपिका:
- **Translation**: 

---

### Verse 3 (Vaivtpuran 92.19301)
- **Original**: लोकास्त्वामेव.. गायन्ति गीतैर्मड्रलसंस्तवै: । त्वत्सुकीति च वेदाश्न सनकाद्माश्च॒संततम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 92.19302)
- **Original**: कृतपापहरां पुण्यां तीर्थपूजां च निर्मलाम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 92.19303)
- **Original**: हरिभक्तिप्रदां. भद्ठां. सर्वविघ्नविनाशिनीम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 92.19304)
- **Original**: त्वमेब राधा त्वं कृष्णस्त्व॑ पुमान्‌ प्राकृति:परा। राधामाधवयोभेंदों न पुराणे श्रुता तथा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 92.19305)
- **Original**: इति अऔब्रह्मवैवर्ते उद्धवकृवा श्रीराधाग्रार्थना सम्पूर्णा। ( श्रीकृष्णजन्मखण्ड 94। 3--7) गणेशकूृतं श्रीराधास्तवनम्‌ श्रीगणेश उवाच तव पूजा जगन्मातर्लोकशिक्षाकरी शुभे । ब्रह्मस्वरूपा भवती कृष्णवक्षःस्थलस्थिता
- **Translation**: 

---

### Verse 8 (Vaivtpuran 92.19306)
- **Original**: वत्पादपद्ममतुल॑ ध्यायन्ते ते सुदुर्लभम्‌ । सुरा ब्रह्मेशशेषाद्या मुनीद्ा: सनकादय:
- **Translation**: 

---

### Verse 9 (Vaivtpuran 92.19307)
- **Original**: जीवन्मुक्ताश्न भक्ताश्न सिद्धेद्रा: कपिलादव: । तस्य प्राणाधिदेवी त्व॑ प्रिया प्राणाधिका परा
- **Translation**: 

---

### Verse 10 (Vaivtpuran 92.19308)
- **Original**: यामाडुनिर्मिता राधा दक्षिणाडुश्न॒ माधव: । पहालक्ष्मीर्जगन्माता_ तब खामाडुनिर्मिता
- **Translation**: 

---

### Verse 11 (Vaivtpuran 92.19309)
- **Original**: वसो: सर्वनिवासस्य प्रसूस््य॑ परमेश्वरी । बेदानां जगतामेवब मूलप्रकृतिरी ध्वरी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 92.19310)
- **Original**: सर्वा: प्राकृतिका मात: सृष्टयां च॒ त्वद्विभूतय:
- **Translation**: 

---

### Verse 13 (Vaivtpuran 92.19311)
- **Original**: विश्वानि कार्यरूपाणि त्व॑ च॒ कारणरूपिणी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 92.19312)
- **Original**: प्रलये , ब्रह्मण: पाते तत्निमेषो हरेरपि । आदौ राधां सपमुच्चार्य पश्चात्‌ कृष्णं परात्परम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 92.19313)
- **Original**: स एवं पण्डितों योगी गोलोक॑ याति लीलया । व्यतिक्रमे महापापी ब्रह्महत्यां लभेद्‌ श्लुबम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 92.19314)
- **Original**: जगतां भवती माता परमात्मा पिता हरि: । पितुरेव गुरुमाता पूज्या वन्‍्च्या परात्परा
- **Translation**: 

---

### Verse 17 (Vaivtpuran 92.19315)
- **Original**: भजते देवमन्यं बा कृष्णं वा सर्वकारणम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 92.19316)
- **Original**: पुण्यक्षेत्रे महामूढह़ो यदि निन्दति राधिकाम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 92.19317)
- **Original**: वंशहानिर्भवेत्तस्य दुःखशोकमिहैव च । पच्यते निरये घोरे यावच्चन्द्रदिवाकरौ
- **Translation**: 

---

### Verse 20 (Vaivtpuran 92.19318)
- **Original**: गुरुश्ष॒ ज्ञानोद्ििरणाजज्नानं॑ स्थान्मन्नतन्त्रयों: । स अर मन्त्रश्न तत्तन्र॑ भक्ति: स्थाद युवयोग्यत:
- **Translation**: 

---

