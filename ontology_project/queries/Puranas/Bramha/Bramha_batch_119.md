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

### Verse 1 (Bramha 0.2361)
- **Original**: आपकी मायाको जानना चाहता हूँ। देवेश! भगवन्‌! आप ही पृथ्वी, आप ही जल, आप ही
- **Translation**: 

---

### Verse 2 (Bramha 0.2362)
- **Original**: आपकी कृपासे मेरी स्मरणशक्ति लुप्त नहीं हुई है। अग्रि और आप हो वायु हैं। जगत्पते! आकाश,
- **Translation**: 

---

### Verse 3 (Bramha 0.2363)
- **Original**: पुण्डरीकाक्ष! आप अव्यय हैं, मैं आपके तत्त्वको मन, अहंकार, बुद्धि, प्रकृति तथा सत्त्वादि गुण भी
- **Translation**: 

---

### Verse 4 (Bramha 0.2364)
- **Original**: समझना चाहता हूँ। इस सम्पूर्ण जगत्‌कों पीकर आप ही हैं। आप सम्पूर्ण विश्वमें व्यापक पुरुष
- **Translation**: 

---

### Verse 5 (Bramha 0.2365)
- **Original**: आप साक्षात्‌ परमेश्वर यहाँ बालरूपसे क्‍यों रहते हैं। पुरुषसे भी उत्तम पुरुषोत्तम हैं । प्रभो! आप ही
- **Translation**: 

---

### Verse 6 (Bramha 0.2366)
- **Original**: हैं? ये सब बातें बतानेकी कृपा करें। सम्पूर्ण इन्द्रियाँ और उनके शब्द आदि विषय हैं। । मुनिके इस प्रकार पूछनेपर परम कान्तिमान्‌ आप ही दिक्‍्पाल, धर्म, वेद, दक्षिणासहित यज्ञ,
- **Translation**: 

---

### Verse 7 (Bramha 0.2367)
- **Original**: देवाधिदेव श्रीहरिने उन्हें सान्त्वना देते हुए इन्द्र, शिव, देवता, हविष्य और अग्नि हैं। वसु,
- **Translation**: 

---

### Verse 8 (Bramha 0.2368)
- **Original**: कहा--' ब्रह्मन्‌ ! देवता भी मुझे ठीक-ठीक नहीं रुद्र, आदित्य और ग्रह भी आपके ही स्वरूप हैं
- **Translation**: 

---

### Verse 9 (Bramha 0.2369)
- **Original**: जानते; किंतु तुमपर प्रेम होनेके कारण मैं अपना और जितनी भी जातियाँ हैं, जो कुछ भी जीव-
- **Translation**: 

---

### Verse 10 (Bramha 0.2370)
- **Original**: रहस्य बतलाऊँगा कि कैसे इस जगत्‌की सृष्टि नामधारी पदार्थ है, वह सब आप ही हैं। अधिक
- **Translation**: 

---

### Verse 11 (Bramha 0.2371)
- **Original**: करता हूँ। ब्रह्म! तुम पितृभक्त हो और मेरी कहनेकी क्या आवश्यकता, ब्रह्मसे लेकर तिनकेतक
- **Translation**: 

---

### Verse 12 (Bramha 0.2372)
- **Original**: शरणमें आये हो; इसीलिये तुम्हें मेरे स्वरूपका जो कुछ भी भूत, भविष्य और बर्तमान चराचर
- **Translation**: 

---

### Verse 13 (Bramha 0.2373)
- **Original**: प्रत्यक्ष दर्शन हुआ है। तुम्हारा ब्रह्मचर्य महान्‌ है। जगत्‌ है, वह आप ही हैं। देव! आपका जो
- **Translation**: 

---

### Verse 14 (Bramha 0.2374)
- **Original**: पूर्वकालमें मैंने जलकों 'नारा' नाम दिया था, उस परमस्वरूप है, वह कूटस्थ, अचल एवं ध्रुव है।
- **Translation**: 

---

### Verse 15 (Bramha 0.2375)
- **Original**: 'नारा' में मेरा सदा अयन (निवास) रहता है उसे ब्रह्मा आदि देवता भी नहीं जान पाते। फिर
- **Translation**: 

---

### Verse 16 (Bramha 0.2376)
- **Original**: इसलिये मैं “नारायण' कहलाता हूँ। द्विजोत्तम! मैं हम-जैसे छोटी बुद्धिवाले मनुष्य कैसे उसका
- **Translation**: 

---

### Verse 17 (Bramha 0.2377)
- **Original**: नारायण ही सबकी उत्पत्तिका कारण, सनातन, तत्त्व समझ सकते हैं। भगवन्‌! आप शुद्धस्वभाव,
- **Translation**: 

---

### Verse 18 (Bramha 0.2378)
- **Original**: अविनाशी, सम्पूर्ण भूतोंका स्रष्टा और संहर्ता हूँ। नित्य, प्रकृतिसे परे, अव्यक्त, शाश्वत, अनन्त एवं
- **Translation**: 

---

### Verse 19 (Bramha 0.2379)
- **Original**: मैं ही विष्णु, मैं ही ब्रह्मा और मैं ही देवराज इन्द्र
- **Translation**: 

---

### Verse 20 (Bramha 0.2380)
- **Original**: 116 + संक्षिप्त ब्रह्मपुराण « हूँ। यक्षराज कुबेर और प्रेतराज यम भी मैं ही हूँ।
- **Translation**: 

---

