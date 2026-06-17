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

### Verse 1 (Vishnu Puran 0.6781)
- **Original**: यबनान्मुण्डितशिरसो$र्ड्धमुण्डिताउ्छकान्‌ प्रल्लम्बकेझान्‌ पारदान्‌_ पह्ववाजदमश्नुधरान्‌ निस्स्वाध्यायवषदकारानेतानन्यांश्च॒.श्षत्रियां- श्वकार
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6782)
- **Original**: एते चात्पधर्मपरित्यागाद्राह्मणै परित्यक्ता म्लेच्छतां ययु:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6783)
- **Original**: सगरे5पि स्वमधिष्ठानमागम्यास्खलितचक्रस्सप्तद्रीपवती - पिमामुर्वी प्रशशास
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6784)
- **Original**: [ आ* 3 उसपर पतिका शब स्थापित कर उसके साथ सती होनेक्य निशय किया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6785)
- **Original**: उसी समय भूत, भविष्यत्‌ और वर्तमान तीनों कालके जाननेवाले भगवान्‌ और्वने अपने आश्रमसे निकककर उससे कहा--+
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6786)
- **Original**: 'अयि साध्वि ! इस व्यर्थ दुग्ग्रहको छोड़। तेरे उदरमें सम्पूर्ण भूमण्डलका स्वामी, अत्यन्त बल-पराक्रमझौल, अनेक यज्ञॉक्ा अनुष्ठान करनेवाल्म और चाबुऑँका नाद्ा करनेवाल्त चक्रवर्ती राजा है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6787)
- **Original**: तू ऐसे दुस्साहसका उद्योग न कर ।' ऐसा कहे जानेपर यह अनुमरण (सती होने) के आयहसे विरत हो गयी
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6788)
- **Original**: और भगवान्‌ और्ब उसे अपने आश्रपपर छे आये
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6789)
- **Original**: यहाँ कुछ ही दिनॉमें, उसके उस गर (विष) के साथ ही एक अति तेजस्त्री ज्रालकने जच्म लिया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6790)
- **Original**: भगवान्‌ और्वने उसके जातकर्म आदि संस्कार कर उसका नाम 'सगर' रखा तथा उसका उपनयनसंस्कार होनेपर और्वने ही उसे बेद, शास्त्र एले भार्गव नामक अग्रेय दास्पोकी दिक्षा दी
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6791)
- **Original**: 36 30। बुद्धिका क्कलस होनेपर उस बालकने अपनी मातासे कहा--
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6792)
- **Original**: “माँ ! यह तो बता, इस तपोयनमें हम क्‍यों रहते हैं और हमारे पिता कहाँ हैं ?'' इसी प्रकारके और भी प्रश्न पूछतेपर माताते उससे सम्पूर्ण वृत्तात्त कह दिया
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6793)
- **Original**: तब तो पिताके राज्यापहरणकों सहन न कर सकनेके कारण उसने हैहय और तालजंघ आदि क्षत्रियोंको मार डालनेकी प्रतिज्ञा की और प्रायः सभी हैहय एवं तालजंघबंशोय ग्रजाओंक्य नष्ट कर दिया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6794)
- **Original**: उनके पश्चात्‌ स्क, यवन, काम्बोज़, पारद और पहवगण भी हताहत होकर सगसके कुलगुरु वरसिष्टजीकी वारणमें गये
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6795)
- **Original**: वसिप्रजीने उन्हे जीवन्पुत (जीते हुए ही मरेके समान) करके सगरसे कहा---' बेट। इन जोते-जी मरे हुओंका पोछा करनेसे क्या स्मभ है ?
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6796)
- **Original**: देख, तेरी प्रतिज्ञाकों पूर्ण करनेके लिये मैंने हो इन्हें स्वधर्म और द्विजातियोंके संसर्गसे वद्धित कर दिया है”
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6797)
- **Original**: राजाने 'जो आज्ञा' कहकर गुरजीके कथनका अनुमोदन किया और उनके बेष बदलवा दिये
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6798)
- **Original**: उसने यवनोंके सिर मुड़बा दिये, शकोंको अर्द्धमुण्डित कर दिया, पारदोंके लम्बे-लम्बे करे रखना दिये, चह्नयोंके मुँछ-दाढ़ी रखता दीं तथा इनको और इनके समान अच्यान्य क्षत्रियोंको मी स्वाध्याय और वषदट्कारादिसे बहिष्कृत कर दिया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6799)
- **Original**: अपने घर्मक्त्रे छोड़ देनेके कारण बाह्यणोंने भी इनका परित्याग कर दिया; अतः ये घ्लेज्छ हो गये
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6800)
- **Original**: तदनत्तर महायज सगर अपनी राजथानोमें आकर अप्रतिहत सैन्यसे युक्त हो इस सम्पूर्ण सप्तद्वीपवती पृथिवीका ज्ञासन करने लगें
- **Translation**: 

---

