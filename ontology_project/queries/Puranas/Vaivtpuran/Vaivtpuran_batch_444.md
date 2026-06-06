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

### Verse 1 (Vaivtpuran 23.1842)
- **Original**: सब देवता प्रकृतिजन्य हैं। वे भक्तिदायिनी जगत्स्नष्टा ब्रह्मा नष्ट हो जाते हैं, उनके कर्मका
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.1843)
- **Original**: श्रीप्रकृतिका भजन करते हैं। प्रकृति ब्रह्मस्वरूपा बर्णन करनेमें भूतलपर कौन समर्थ है? तुम भी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.1844)
- **Original**: है। वह ब्रह्मसे भिन्न नहीं है। उसीके द्वारा सनातन श्रीहरिके चरणारविन्दका अत्यन्त आदरपूर्वक
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.1845)
- **Original**: पुरुष परमात्मा संसारकी सृष्टि करते हैं, श्रीप्रकृतिकी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.1846)
- **Original**: डे क संक्षिप्त ख्रह्मवैवर्तपुराण के %$%%%$%%$%%%%%$%%$%$%%$%%$%$%%%% 55% 55% #%%###%#### 55% % %%%%% %% % % %%% % ऋक के कलासे ही संसारकी सारी स्त्रियाँ प्रकट हुई हैं।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.1847)
- **Original**: प्रकृतिदेवी ही अपमानित होती हैं। जिसने पति- प्रकृति ही माया है, जिसने सबको मोहमें डाल
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.1848)
- **Original**: पुत्रसे युक्त सती-साध्वी दिव्य नारीका पूजन रखा है। वह सनातनी परमा प्रकृति नारायणी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.1849)
- **Original**: किया है, उसके द्वारा सर्वमड्रलदायिनी प्रकृतिदेवीका कही गयी है; क्योंकि बह परमपुरुष नारायणकी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.1850)
- **Original**: ही पूजन सम्पन्न हुआ है। मूल प्रकृति एक ही शक्ति है। सर्वात्मा ईश्वर भी उसीके द्वारा
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.1851)
- **Original**: है। बह पूर्ण ब्रह्मस्वरूपिणी है। उसोको सनातनी शक्तिमान्‌ होते हैं। उस शक्तिके बिना वे सृष्टि
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.1852)
- **Original**: विष्णुमाया कहा गया है। सृष्टिकालमें बह पाँच करनेमें सदा असमर्थ ही हैं। वत्स! तुम इस
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.1853)
- **Original**: रूपॉमें प्रकट होती है। जो परमात्मा श्रीकृष्णके समय जाकर विवाह करो। मैं तुम्हें पिताके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.1854)
- **Original**: प्राणॉँकी अधिष्ठात्री देवी है तथा समस्त प्रकृतियोंमें आदेशका पालन करनेकी आज्ञा देता हूँ। जो उन्हें सबसे अधिक प्यारी है, उस मुख्या गुरुकी आज्ञाका पालन करनेवाला है, वह सदा
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.1855)
- **Original**: प्रकृतिका नाम “राधा है। दूसरी प्रकृति नारायणप्रिया सर्वत्र पूजनीय तथा विजयी होता है। जो पुरुष
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.1856)
- **Original**: लक्ष्मी हैं, जो सर्वसम्पत्स्वरूपिणी हैं। तीसरी वस्त्र, अलंकार और चन्दनसे अपनी पत्रोका
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.1857)
- **Original**: प्रकृति बाणीकी अधिष्ठात्री देवी सरस्वती हैं, जो सत्कार करता है, उसपर प्रकृतिदेवी संतुष्ट होती
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.1858)
- **Original**: सदा सबके द्वारा पूजनीया हैं। चौथी प्रकृति हैं। ठीक उसी तरह जैसे ब्राह्मणकी पूजा-अर्चा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.1859)
- **Original**: बेदमाता सावित्री हैं। वे ब्रह्माजीकी प्यारी पत्नी करनेपर भगवान्‌ श्रीकृष्ण संतुष्ट होते हैं। प्रकृति
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.1860)
- **Original**: और सबकी पूजनीया हैं। पाँचवीं प्रकृतिका नाम ही सम्पूर्ण लोकॉमें अपनी मायासे स्त्रियोंक रूपमें दुर्गा है, जो भगवान्‌ शंकरकी प्यारी पत्नी हैं। प्रकट हुई हैं। अत: महिलाओंके अपमानसे वे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.1861)
- **Original**: उन्हींके पुत्र गणेश हैं। (अध्याय 30) #30#<00< कल 202/352/-0050
- **Translation**: 

---

