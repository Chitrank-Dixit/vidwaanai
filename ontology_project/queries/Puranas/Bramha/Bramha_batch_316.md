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

### Verse 1 (Bramha 0.6301)
- **Original**: मूर्तिमान्‌ बैठा देखता हूँ। यह परम आक्षर्यमय उन सबके द्वारा आपका ही बोध होता है। आप ही
- **Translation**: 

---

### Verse 2 (Bramha 0.6302)
- **Original**: जगत्‌ जिन महात्माका स्वरूप है, उन्हीं आश्चर्यस्वरूप देवता हैं, सम्पूर्ण जगत्‌ हैं तथा विश्वरूप हैं।
- **Translation**: 

---

### Verse 3 (Bramha 0.6303)
- **Original**: आपके साथ मेरा समागम हुआ है। मधुसूदन! विश्वात्मन्‌ ! आप विकार और भेदसे सर्वथा रहित
- **Translation**: 

---

### Verse 4 (Bramha 0.6304)
- **Original**: अब इस विषयमें अधिक कहनेकी क्या आवश्यकता। हैं, सम्पूर्ण विश्वमें आपके सिवा दूसरी कोई वस्तु ' चलिये, मथुरा चलें। मैं कंससे डरता हूँ। जो नहीं है। आप ही ब्रह्मा, महादेवजी, सूर्य, धाता,
- **Translation**: 

---

### Verse 5 (Bramha 0.6305)
- **Original**: दूसरॉके टुकड़ोंपर जीवन-निर्वाह करनेवाले हैं, विधाता, इन्द्र, वायु, अग्नि, वरुण, कुबेर और यम
- **Translation**: 

---

### Verse 6 (Bramha 0.6306)
- **Original**: उन मनुष्योंके जन्मको धिकार है। हैं। एकमात्र आप हो भिन्न-भिन्न रूप धारण करके
- **Translation**: 

---

### Verse 7 (Bramha 0.6307)
- **Original**: . यों कहकर अक्रूरने घोड़ोंको हाँक दिया और अपनी विभिन्न शक्तियोंसे जगत्‌की रक्षा करते हैं। सायंकालके समय मधथुरापुरीमें जा पहुँचे। मथुराको आप ही विश्वकी सृष्टि करते हैं और आप ही
- **Translation**: 

---

### Verse 8 (Bramha 0.6308)
- **Original**: देखकर अक्रूरने बलराम और श्रोकृष्णसे कहा- प्रलयकालीन सूर्य होकर सम्पूर्ण जगत्‌का संहार
- **Translation**: 

---

### Verse 9 (Bramha 0.6309)
- **Original**: 'महापराक्रमी वीरो! अब आपलोग पैदल जाइये। करते हैं। अज! यह गुणमय प्रपक्ष आपका ही
- **Translation**: 

---

### Verse 10 (Bramha 0.6310)
- **Original**: रथसे मैं अकेला ही जाऊँगा। मधथुरामें पहुँचकर
- **Translation**: 

---

### Verse 11 (Bramha 0.6311)
- **Original**: 304 * संक्षिप्त श्रह्मपुराण * आप दोनों वसुदेवजीके घर न जायें, क्योंकि
- **Translation**: 

---

### Verse 12 (Bramha 0.6312)
- **Original**: मेरे घर पधारे हैं! मैं धन्य हो गया। अब पुष्पोंसे आपके ही कारण वह बेचारा बूढ़ा कंसके द्वार
- **Translation**: 

---

### Verse 13 (Bramha 0.6313)
- **Original**: आप दोनोंकी पूजा करूँगा।' यों कहकर उसने सदा अपमानित होता है।'
- **Translation**: 

---

### Verse 14 (Bramha 0.6314)
- **Original**: रुचिके अनुसार फूल भेंट किये। “ये सुन्दर हैं, ये यों कहकर अक्रूर मथुरापुरीमें चले गये।
- **Translation**: 

---

### Verse 15 (Bramha 0.6315)
- **Original**: मनोहर हैं,' यों कहते हुए उसने उनके मनमें राम और श्रोकृष्ण भी पुरीमें पहुँचकर राजमार्गपर
- **Translation**: 

---

### Verse 16 (Bramha 0.6316)
- **Original**: फूलोंके प्रति आकर्षण पैदा किया और जो-जो आ गये। उस समय नगरके सभी स्थ्री-पुरुष , उन्हें पसंद आया, वह सब दिया। प्राय: सभी फूल आनन्दपूर्ण नेत्नोंसे उन्हें निहारते थे। वे दोनों
- **Translation**: 

---

### Verse 17 (Bramha 0.6317)
- **Original**: मनोहर, निर्मल और सुगन्धित थे। श्रीकृष्णने भी यौर तरुण हाथियोंकी भाँति लीलापूर्वक चल
- **Translation**: 

---

### Verse 18 (Bramha 0.6318)
- **Original**: 'आउयाक या 8 रहे थे। घूमते-घूमते उन दोनों भाइयोंने कपड़ा
- **Translation**: 

---

### Verse 19 (Bramha 0.6319)
- **Original**: रैगनेवाले एक रजककों देखा। उससे अपने शरीरके अनुरूप सुन्दर वस्त्र माँगे। वह राजा अहंकार बहुत बढ़ गया था। उसने बलराम और श्रीकृष्णके प्रति ललकारकर अनेक आशक्षेपयुक्त कटुवचन कहे। उस दुरात्मा रजकका बूर्ताव देख श्रीकृष्ण क्ुपित हो उठे। उन्होंने थप्पड़से
- **Translation**: 

---

### Verse 20 (Bramha 0.6320)
- **Original**: मारकर उस रजकका मस्तक पृथ्वीपर गिरा
- **Translation**: 

---

