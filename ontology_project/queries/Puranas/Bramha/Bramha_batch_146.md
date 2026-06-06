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

### Verse 1 (Bramha 0.2901)
- **Original**: . विष्णु बोले--दैत्यराज! देखो, मैं पैर बढ़ाता हूँ। लेकर बैठे थे और हविष्यका हवन करते हुए
- **Translation**: 

---

### Verse 2 (Bramha 0.2902)
- **Original**: बलिने कहा--बढ़ाइये, अवश्य बढ़ाइये। यज्ञपुरुषका ध्यान कर रहे थे। शुक्राचार्यजीने
- **Translation**: 

---

### Verse 3 (Bramha 0.2903)
- **Original**: . तब भगवानने पृथ्वीके नीचे स्थित कच्छपकी वामनजीको पहचानकर तुरंत हो राजा बलिसे
- **Translation**: 

---

### Verse 4 (Bramha 0.2904)
- **Original**: पीठपर पैर रखकर पहला पग बलिके यज्ञमें रखा, कहा--'राजन्‌! ये जो बौने शरीरवाले ब्राह्मण
- **Translation**: 

---

### Verse 5 (Bramha 0.2905)
- **Original**: किंतु उनका दूसरा पग ब्रह्मलोकतक जा पहुँचा। तुम्हारे यज्ञमें आये हैं, वे वास्तबपें ब्राह्मण नहीं,
- **Translation**: 

---

### Verse 6 (Bramha 0.2906)
- **Original**: उस समय उन्होंने बलिसे कहा--' दैत्यराज! मेरा यज्ञवाहन यज्ञेश्वर विष्णु हैं। प्रभो! इसमें तनिक
- **Translation**: 

---

### Verse 7 (Bramha 0.2907)
- **Original**: तीसरा पग रखनेके लिये तो स्थान ही नहों है, संदेह नहीं कि थे देबताओंका हित करनेके लिये
- **Translation**: 

---

### Verse 8 (Bramha 0.2908)
- **Original**: कहाँ रखूँ? स्थान दो।' बालकरूप धारणकर तुमसे कुछ याचना करने
- **Translation**: 

---

### Verse 9 (Bramha 0.2909)
- **Original**: . यह सुनकर बलिने हँसते हुए कहा--'जगन्मय आये हैं। अतः पहले मुझसे सलाह लेकर पीछे
- **Translation**: 

---

### Verse 10 (Bramha 0.2910)
- **Original**: देवेश्वर! आपने ही तो जगत्‌कौ सृष्टि की है, मैं इन्हें कुछ देना चाहिये।' तो इसका स्रष्टा नहीं हूँ। यदि यह छोटा या थोड़ा यह सुनकर शत्रुविजयी बलिने अपने पुरोहित
- **Translation**: 

---

### Verse 11 (Bramha 0.2911)
- **Original**: हो गया तो इसमें आपका ही दोष है, मैं क्या शुक्राचार्यसे कहा--“मैं धन्य हूँ, जिसके घरपर
- **Translation**: 

---

### Verse 12 (Bramha 0.2912)
- **Original**: करूँ। केशव! फिर भी मैं कभी असत्य नहीं साक्षात्‌ यज्ञेश्वर मूर्तिमान्‌ होकर पधारते और कुछ
- **Translation**: 

---

### Verse 13 (Bramha 0.2913)
- **Original**: बोलता, अत: मेरे सत्यकी रक्षा करते हुए आप याचना करते हैं। अब इसमें सलाह लेनेके योग्य
- **Translation**: 

---

### Verse 14 (Bramha 0.2914)
- **Original**: अपना तीसरा पग मेरी पीठपर ही रखिये।' कौन-सी बात रह जाती है।' यों कहकर पत्नी
- **Translation**: 

---

### Verse 15 (Bramha 0.2915)
- **Original**: बलिका यह वचन सुनकर बेदत्रयीरूप देवपूजित और पुरोहित शुक्राचार्यके साथ राजा बलि उस
- **Translation**: 

---

### Verse 16 (Bramha 0.2916)
- **Original**: भगवान्‌ प्रसन्न होकर बोले--' दैत्यराज! मैं तुम्हारी स्थानपर आये, जहाँ अदितिनन्दन वामनजी विराजमान
- **Translation**: 

---

### Verse 17 (Bramha 0.2917)
- **Original**: भक्तिसे बहुत प्रसन्न हूँ। तुम्हारा कल्याण हो, कोई थे। राजाने हाथ जोड़कर पूछा--' भगवन्‌ ! बताइये,
- **Translation**: 

---

### Verse 18 (Bramha 0.2918)
- **Original**: वर माँगो।' तब बलिने जगत्‌्के स्वामी भगवान्‌ आप क्या चाहते हैं?' तब वामनजीने कहा-
- **Translation**: 

---

### Verse 19 (Bramha 0.2919)
- **Original**: त्रिविक्रमसे कहा-'अब मैं आपसे याचना नहीं “महाराज! केवल तीन पग भूमि दे दीजिये और
- **Translation**: 

---

### Verse 20 (Bramha 0.2920)
- **Original**: करूँगा।' तब भगबानूने स्वयं ही प्रसन्न होकर किसी धनको मुझे आवश्यकता नहीं है।' “बहुत
- **Translation**: 

---

