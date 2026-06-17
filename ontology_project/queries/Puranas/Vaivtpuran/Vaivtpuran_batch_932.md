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

### Verse 1 (Vaivtpuran 543.16954)
- **Original**: विश्व-समूहका विनाश कर सकते हैं; फिर इस शिवसे बोला। नगरकी तो बात ही क्‍या है। अतः तुम सब मणिभद्गने कहा--महे श्वर ! बलदेव, प्रद्यु्र,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.16955)
- **Original**: लोग सभी उपायोंद्वारा यत्रपूर्वक्त बाणकी रक्षा साम्ब, सात्यकि, महाराज उग्रसेन, स्वयं भीम,
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.16956)
- **Original**: करो। अब बाण लम्बोदर गणेशका स्मरण करके अर्जुन, अक्रूर, उद्धव और शक्रनन्दन जयन्त तथा
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.16957)
- **Original**: संग्रामभूमिको जाय। उसके दक्षिणभागमें स्कन्द, जो विधिके भी विधाता हैं, जिनकी कान्ति करोड़ों
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.16958)
- **Original**: आगे-आगे गणेश्वर और वामभागमें आठों भैरव, कामदेबोंकी शोभाकों छोने लेती है, बनमाला
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.16959)
- **Original**: एकादश रुद्र, स्वयं महारथी नन्‍्दी, महाकाल, जिनकी शोभा बढ़ा रही है, सात गोप-पार्षद श्वेत
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.16960)
- **Original**: वीरभद्र तथा अन्यान्य सैनिक उसकी रक्षा करें। चँवरोंद्रार जिनको सेवा कर रहे हैं, जो करोड़ों
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.16961)
- **Original**: ऊर्ध्वभागमें दुर्गा, भद्रकाली, उग्रचण्डा और सूर्योके समान कान्तिमानू अनुपम चक्र धारण
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.16962)
- **Original**: कोटरीको रहना चाहिये। दुर्गतिनाशिनी दुर्गे! करते हैं; वे परमेश्वर भगवान्‌ श्रीकृष्ण बहुमूल्य
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.16963)
- **Original**: बाणकी रक्षा करो। महाभागे! तुम्हीं श्रीकृष्णकी रत्नोंके सारभागसे निर्मित परम रमणीय उत्तम
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.16964)
- **Original**: शक्ति हो; इसीलिये “नारायणी' कही जाती हो। रथमें कौमोदकी गदा, अमोध शूल और विश्वसंहारकारी । विष्णुमाये
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.16965)
- **Original**: तुम जगज्जननी तथा सम्पूर्ण मड्गलोंकी महाशह्लु पाक्षजन्य रखकर यादबोंकी असंख्य
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.16966)
- **Original**: भी मड्गलस्वरूपा हो; अतः चक्रोंके साररूप
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.16967)
- **Original**: 750 + संक्षिप्त ब्रह्मवैवर्तपुराण « कऋडऋ 55 #ऋऋ#ऋ##
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.16968)
- **Original**: 84948 ######8##8#######%#%#&%#%&%$#%$#%$%$%$4$5%%$%%$%%$%%%क%%%%%%% कक अमोघ सुदर्शनचक्रसे बाणको बचाओ; क्योंकि
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.16969)
- **Original**: सामने कौन ठहर सकता है? श्रीकृष्ण सबके बाण मुझे गणेश, कार्तिकेय आदि सभीसे भी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.16970)
- **Original**: परमात्मा, भक्तानुग्रहमूर्ति, नित्य, सत्य, परिपूर्णतम बढ़कर प्रिय है। अत: बाणके मस्तकपर तुम
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.16971)
- **Original**: प्रभु हैं। गणेश और कार्तिकेय तथा उन दोनोंसे अपने चरणकमलकी रजके साथ-साथ अपना
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.16972)
- **Original**: भी परे आप मेरे लिये प्रिय हैं और किंकरोंमें वरद हस्त स्थापित करो। शिवजीका कथन
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.16973)
- **Original**: बाण प्रिय है; किंतु श्रीकृष्णसे बढ़कर प्यारा दूसरा सुनकर दुर्गतिनाशिनी दुर्गा मुस्करा्यीं और समयोचित
- **Translation**: 

---

