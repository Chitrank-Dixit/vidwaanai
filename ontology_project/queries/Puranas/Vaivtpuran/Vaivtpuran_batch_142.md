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

### Verse 1 (Vaivtpuran 8.6400)
- **Original**: मारकर हँस पड़ा। (अध्याय 11) +2000गीव्यिधषया(020000 पार्वतीके कहनेसे शनैश्वरका गणेशपर दृष्टिपात करना, गणेशके सिरका कटकर गोलोकमें चला जाना, पार्वतीकी मूर्च्छा, श्रीहरिका आगमन और गणेशके धड़पर हस्तीका सिर जोड़कर जीवित करना, फिर पार्वतीको होशमें लाकर बालकको आशीर्वाद देना, पार्वतीद्वारा शनैश्षरको शाप श्रीनारायणजी कहते हैं--नारद ! शनैश्षरका
- **Translation**: 

---

### Verse 2 (Vaivtpuran 8.6401)
- **Original**: मस्तक धड़से अलग हो गया। तब शबनैश्वरने वचन सुनकर दुर्गाने परमेश्वर श्रीहरिका स्मरण
- **Translation**: 

---

### Verse 3 (Vaivtpuran 8.6402)
- **Original**: / क्ष 36 56 शी! ही! किया और “सारा जगत्‌ ईश्वरकी इच्छाके वशीभूत
- **Translation**: 

---

### Verse 4 (Vaivtpuran 8.6403)
- **Original**: ही है' यों कहा। फिर दैववशीभूता पार्वतीदेवीने कौतूहलवश शबनैश्वरसे कहा--'तुम मेरी तथा मेरे बालककी ओर देखो। भला, इस निषेक (कर्मफलभोग)-को कौन हटा सकता है?' तब पार्वतीका वचन सुनकर शबनैश्वर स्वयं मन-ही- मन यों विचार करने लगे--'अहो! क्‍या मैं इस पार्वतीनन्दनपर दृष्टिपात करूँ अथवा न कहूँ? क्योंकि हु हैं, / 5 5 यदि मैं बालकको देख लूँगा तो निश्चय ही उसका
- **Translation**: 

---

### Verse 5 (Vaivtpuran 8.6404)
- **Original**: 3.8 बा अनिष्ट हो जायगा।' यों कहकर धर्मात्मा शनैश्वरने
- **Translation**: 

---

### Verse 6 (Vaivtpuran 8.6405)
- **Original**: अपनी आँख फेर ली और फिर वे नीचे मुख धर्मको साक्षी बनाकर बालकको तो देखनेका
- **Translation**: 

---

### Verse 7 (Vaivtpuran 8.6406)
- **Original**: करके खड़े हो गये। इसके बाद उस बालकका विचार किया, परंतु बालककी माताकों नहीं।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 8.6407)
- **Original**: खूनसे लथपथ हुआ सारा शरीर तो पार्वतीकी शनैश्वरका मन तो पहलेसे ही ख्न्न था। उनके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 8.6408)
- **Original**: गोदमें पड़ा रह गया, परंतु मस्तक अपने अभीष्ट कण्ठ, ओष्ठ और तालु भी सूख गये थे; फिर भी
- **Translation**: 

---

### Verse 10 (Vaivtpuran 8.6409)
- **Original**: गोलोकमें जाकर श्रीकृष्णमें प्रविष्ट हो गया। यह उन्होंने अपने बायें नेत्रके कोनेसे शिशुके मुखकी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 8.6410)
- **Original**: देखकर पार्वतीदेवी बालककों छातीसे चिपटाकर ओर निहारा। मुने ! शनिकी दृष्टि पड़ते ही शिशुका फूट-फूटकर बिलाप करने लगीं और उन्मत्तकी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 9.2207)
- **Original**: कर प्रकृतिखण्ड 9 101
- **Translation**: 

---

### Verse 13 (Vaivtpuran 9.2208)
- **Original**: 334 3. सरस्वतीकी पूजाका विधान तथा कवच नारदजीने कहा--भगवन्‌! आपके कृपा-
- **Translation**: 

---

### Verse 14 (Vaivtpuran 9.2209)
- **Original**: परिणाममें सुख देनेवाले बचन कहे। प्रसादसे यह अमृतमयी सम्पूर्ण कथा मुझे सुननेको भगवान्‌ श्रीकृष्ण बोले--साध्वी! तुम मिली है। अब आप इन प्रकृतिसंज्ञक देवियोंके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 9.2210)
- **Original**: नारायणकी सेवा स्वीकार करो। बे मेरे हो अंश पूजनका प्रसंग विस्तारके साथ बतानेकी कृपा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 9.2211)
- **Original**: हैं। उनकी चार भुजाएँ हैं। उन परम सुन्दर तरुण कीजिये। किस पुरुषने किन देवीकी कैसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 9.2212)
- **Original**: पुरुषमें मेरे ही समान सभी सदुण वर्तमान हैं। आराधना कौ है ? मर्त्यलोकमें किस प्रकार उनकी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 9.2213)
- **Original**: करोड़ों कामदेवोंके समान उनकी सुन्दरता है। बे पूजाका प्रचार हुआ ? मुने! किस मन्त्रसे किनको
- **Translation**: 

---

### Verse 19 (Vaivtpuran 9.2214)
- **Original**: कामिनियोंकी कामना पूर्ण करनेमें समर्थ हैं। मैं पूजा तथा किस स्तोत्रसे किनकी स्तुति की गद्यो
- **Translation**: 

---

### Verse 20 (Vaivtpuran 9.2215)
- **Original**: सबका स्वामी हूँ। सभी मेरा अनुशासन मानते है? किन देवियोंने किनको कौन-कौन-से वबर
- **Translation**: 

---

